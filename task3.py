# -*- coding: utf-8 -*-
#!/usr/bin/python

import math
import time


class Tag:
    count = 1
    weight = 0
    order = 0
    
    def setWeight(self, newWeight):
        self.weight = newWeight
        
    def increment(self):
        self.count +=1

    def __init__ (self, tagOrder):
        self.order = tagOrder
        

timeOpen = time.clock()

with open('10000.txt', 'r') as content_file:
        images = [line.strip().split(" ") for line in content_file]
        

timeClose = time.clock()

print ("Reading file time:" + str(timeClose - timeOpen))

numberOfImages = len(images);
tagDictionary = {}
    
tagcounter = 0    
for image in images:
    for tag in image:
        if tag in tagDictionary:
            tagDictionary[tag].increment()
        else:
            tagDictionary[tag]=Tag(tagcounter)
            tagcounter +=1
          
          
timeDictionary = time.clock() 
print ("Dictionary time :" + str(timeDictionary- timeClose)) 

#print("1")          
#DEBUG
#print(len(tagDictionary))

numberOfTags = len(tagDictionary)
print("The problem has + " + str(numberOfImages) + " images and " + str(numberOfTags) + " tags")

for tag in tagDictionary:
    tagDictionary[tag].setWeight(math.log(numberOfImages) - math.log(tagDictionary[tag].count))
    
    #DEBUG
    #print (tag + " ")
    #print (tagDictionary[tag].weight)

timeWeight = time.clock()  
print ("Weight time :" + str(timeWeight - timeDictionary)) 

#DEBUG
#print(numberOfTags)

#print("2")
          
imageSpace = [];
optimizedImageSpace =[]
maskSpace = []

for image in images:
    
    vector = {}
    newVector = []
    pointer = len(optimizedImageSpace)
    maskSpace.append(0b0)
    optimizedImageSpace.append(newVector)

    norm = 0 
    for tag in image:
       norm += math.pow(tagDictionary[tag].weight,2)
    
    norm = math.sqrt(norm)
    
    tempList = []
    
    for tag in image:

        weightList = []
        order= tagDictionary[tag].order
        vector [order] = tagDictionary[tag].weight / norm
        
        if not vector[order] == 0:
             weightList.append(vector[order])
             weightList.append(order)
             tempList.append(weightList)
             a = 0b1
             a = a << order
             maskSpace[pointer] = maskSpace[pointer] | a

    tempList.sort(key = lambda x: x[0], reverse=True)
    optimizedImageSpace[pointer] = []
    for i in tempList:
        optimizedImageSpace[pointer].append(i[1])
    
    imageSpace.append(vector)    

timeNormalize = time.clock()  
print ("Normalizing time :" + str(timeNormalize - timeWeight)) 

#DEBUG
#print(imageSpace)
#print(optimizedImageSpace)

#print("3")          
def similarity (i , z, threshold, accuracy):
    sim = 0
    size = len(optimizedImageSpace[i])
    count = 0
    for j in optimizedImageSpace[i]:
        if j in imageSpace[z]:
            a = imageSpace[i][j] * imageSpace[z][j]
            sim += a
            #List is ordered. At max, the total similarity will be length of the smaller list times the current value a
            if (sim  + (a * len(optimizedImageSpace[i])-count))  < threshold:
                return False
          
            # Abort computation as soon as possible  #Worse results...
            if(sim >= threshold):
                return True
            
        count +=1 
    
        if count/size > size :
            return (sim >= threshold * accuracy)


def commonTags  (i, z):
    
    #return (maskSpace[i] & maskSpace[z])
    count = 0
    for j in optimizedImageSpace[i]:
        if j in imageSpace[z]:   #O(1)
            return True
    return False        


def similarityCount (threshold, accu):
    count = 0
    for i in range (0, numberOfImages):
        #print (i)
        for z in range (0, i):
            #if(commonTags(i,z)):  
            if similarity (i,z, threshold, accu):
                count += 1
    return count


timeSimilarity1 = time.clock()  
a = similarityCount(0.5, 0.5)
timeSimilarity = time.clock()
print(a)
print ("Similiarity time for:" + str(timeSimilarity - timeSimilarity1))


#fTime = open('time.csv', 'w')
#fResult = open('results.csv', 'w')

#t = 0.01
#print (t)
#while t < 1:
#    timeSimilarity1 = time.clock()  
#    a = similarityCount(t)
#    timeSimilarity = time.clock()
#    
#    print ("Similiarity time for " + str(t) + " :" + str(timeSimilarity - timeSimilarity1))
#    fTime.write(str(t) + "," + str(timeSimilarity - timeSimilarity1) + "\n")
#    fResult.write(str(t) + "," + str(a) + "\n")
#    
#    t = t + 0.01
#
#fTime.close()
#fResult.close()




#i = 1
#while not i <= 0:
#    timeSimilarity1 = time.clock()  
#    print (similarityCount (i))
#    timeSimilarity = time.clock()
#    print ("Similiarity time for " + str(i) + " : " + str(timeSimilarity - timeSimilarity1))
#    i = i - 0.01




 