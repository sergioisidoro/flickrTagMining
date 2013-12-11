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

with open('dataset_small.txt', 'r') as content_file:
        images = [line.strip().split(" ") for line in content_file]
        

timeClose = time.clock()

print ("Reading file time:" + str(timeClose - timeOpen))

numberOfImages = len(images);
tagDictionary = {}
    
tagcounter = 0    
for image in images:
    for tag in image:
        
        if tag in tagDictionary.keys():
            tagDictionary[tag].increment()
        else:
            tagDictionary[tag]=Tag(tagcounter)
            tagcounter +=1
          
          
timeDictionary = time.clock() 
print ("Dictionary time :" + str(timeDictionary- timeClose)) 

#print("1")          
#DEBUG
print(len(tagDictionary))

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
    
    vector = listofzeros = [0] * numberOfTags
    newVector = []
    pointer = len(optimizedImageSpace)
    maskSpace.append(0b0)
    optimizedImageSpace.append(newVector)

    norm = 0 
    for tag in image:
       norm += math.pow(tagDictionary[tag].weight,2)
    
    norm = math.sqrt(norm)
    
    for tag in image:
        order=tagDictionary[tag].order
        vector [order] = tagDictionary[tag].weight / norm
        if not vector[order] == 0:
             optimizedImageSpace[pointer].append(order)
             a = 0b1
             a = a << order
             maskSpace[pointer] = maskSpace[pointer] | a
        
    imageSpace.append(vector)    

timeNormalize = time.clock()  
print ("Normalizing time :" + str(timeNormalize - timeWeight)) 
#DEBUG
#print(imageSpace)
#print(optimizedImageSpace)

#print("3")          
def similarity (i , z, threshold):
    sim = 0
    for j in optimizedImageSpace[i]:
        sim += imageSpace[i][j] * imageSpace[z][j]
        
    #for i in range (0, numberOfTags):
    #    sim += imageSpace[v1][i] * imageSpace[v2][i]
    return sim


def commonTags  (i, z):
    return (maskSpace[i] & maskSpace[z])
    
    #for j in optimizedImageSpace[i]:
    #    if not imageSpace[z][j] == 0:
    #        return True 
    #return False        


def similarityCount (threshold):
    count = 0
    for i in range (0, numberOfImages):
        for z in range (0, i):
            #if z % 1000 == 0:
            #    print(str(i) + " " + str(z))
                
            if(commonTags(i,z)):
            
                if similarity (i,z, threshold) >= threshold:
                    count += 1
    return count

timeSimilarity1 = time.clock()  
print("Result:")
print (similarityCount (0.5))
timeSimilarity = time.clock()
print ("Similiarity time for: " + str(timeSimilarity - timeSimilarity1))

#i = 1
#while not i <= 0:
#    timeSimilarity1 = time.clock()  
#    print (similarityCount (i))
#    timeSimilarity = time.clock()
#    print ("Similiarity time for " + str(i) + " : " + str(timeSimilarity - timeSimilarity1))
#    i = i - 0.01




 