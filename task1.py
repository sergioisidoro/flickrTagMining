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
        

with open('pics_tags.txt', 'r') as content_file:
        images = [line.strip().split(" ") for line in content_file]
        

numberOfImages = len(images);
tagDictionary = {}
    

tagcounter = 0    
for image in images:
    for tag in image:
        if tag in tagDictionary:
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

    vector = {}
    norm = 0 
    for tag in image:
       norm += math.pow(tagDictionary[tag].weight,2)
    
    norm = math.sqrt(norm)
    
    for tag in image:
        vector [tagDictionary[tag].order] = tagDictionary[tag].weight / norm
        
    imageSpace.append(vector)    

#DEBUG
#print(imageSpace)

######################   ###   ################################

#Task 1.1 - Number of photos for each tag

f = open('photos_for_each_tag.txt', 'w')

maximum = 0
for tag in tagDictionary:
     maximum = max(maximum, tagDictionary[tag].count )
     f.write(str(tagDictionary[tag].order) + ";" + str(tagDictionary[tag].count) + "\n")

maximum +=1 

f.close()
##############################   ###   ################################

# Task 1.1 - Number of tags that appear in X photos")

f = open('tags_in_each_photo.csv', 'w')

tagDistribution =[0]* (maximum)

for tag in tagDictionary:
     tagDistribution[tagDictionary[tag].count] += 1


for i in range(0,maximum):
    f.write(str(tagDistribution[i]) + "," + str (i) +"\n")

######################   ###   ################################

## Task 1.1 - Cumulative distribution"

f = open('cumulative_distribution.csv', 'w')

cumulative= [0] * (maximum)
cumulative[0] = tagDistribution[0]

for i in range (1, maximum):
    cumulative[i] = cumulative[i-1] + tagDistribution[i]

for i in range(0,maximum):
    f.write(str (i) + "," + str(cumulative[i]) + "\n")

f.close()
######################   ###   ################################

# Task 1.2 - Image vector in tag space

#for image in imageSpace:
#    print (image)
