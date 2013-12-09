# -*- coding: utf-8 -*-
#!/usr/bin/python

import math

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
        

with open('dataset_small.txt', 'r') as content_file:
        images = [line.strip().split(" ") for line in content_file]
        

numberOfImages = len(images);
tagDictionary = {}
    

tagcounter = 0    
for image in images:
    for tag in image:
        if tag in tagDictionary.keys():
            tagDictionary[tag].increment()
        else:
            tagDictionary[tag] = Tag(tagcounter)
            tagcounter +=1
            
            
#DEBUG
#print(tagDictionary)

numberOfTags = len(tagDictionary)

for tag in tagDictionary:
    tagDictionary[tag].setWeight(math.log(numberOfImages) - math.log(tagDictionary[tag].count))
    
    #DEBUG
    #print (tag + " ")
    #print (tagDictionary[tag].weight)

#DEBUG
#print(numberOfTags)


imageSpace = [];
for image in images:

    vector = listofzeros = [0] * numberOfTags
    
    norm = 0 
    for tag in image:
       norm += math.pow(tagDictionary[tag].weight,2)
    
    norm = math.sqrt(norm)
    
    for tag in image:
        vector [tagDictionary[tag].order] = tagDictionary[tag].weight / norm
        
    imageSpace.append(vector)    

#DEBUG
#print(imageSpace)


def similarity (v1 , v2):
    sim = 0
    for i in range (0, numberOfTags):
        sim += imageSpace[v1][i] * imageSpace[v2][i]
    
    return sim



def similarityCount (threshold):
    count = 0
    for i in range (0, numberOfImages):
        for z in range (0, numberOfImages):
            print(str(i))
            if similarity (i,z) >= threshold:
                count += 1
    return count


print (similarityCount (0.5))

