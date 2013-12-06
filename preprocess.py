# -*- coding: utf-8 -*-
#!/usr/bin/python

import math

class Tag:
    count = 1
    weight = 0
    
    def setWeight(self, newWeight):
        self.weight = newWeight
        
    def increment(self):
        self.count +=1


with open('dataset_small.txt', 'r') as content_file:
        images = [line.strip().split(" ") for line in content_file]
        

numberOfImages = len(images);
tagDictionary = {}
    
    
for image in images:
    for tag in image:
        if tag in tagDictionary.keys():
            tagDictionary[tag].increment()
        else:
            tagDictionary[tag] = Tag()
            
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