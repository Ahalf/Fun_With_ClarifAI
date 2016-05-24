from clarifai.client import ClarifaiApi
from random import randint
import pprint

clarifai_api = ClarifaiApi()
result = clarifai_api.tag_images([open('/Users/adamhalfaker/Documents/PhotosForAI/IMG_0835.JPG', 'rb'),
	open('/Users/adamhalfaker/Documents/PhotosForAI/IMG_0851.JPG','rb'), open('/Users/adamhalfaker/Documents/PhotosForAI/IMG_0873.JPG', 'rb'), 
	open('/Users/adamhalfaker/Documents/PhotosForAI/IMG_0878.JPG', 'rb'), open('/Users/adamhalfaker/Documents/PhotosForAI/IMG_0912.JPG', 'rb'), 
	open('/Users/adamhalfaker/Documents/PhotosForAI/IMG_0926.JPG', 'rb'), open('/Users/adamhalfaker/Documents/PhotosForAI/IMG_0943.JPG', 'rb')])

pp = pprint.PrettyPrinter(indent=1)
wordList = []
finalWordList = []
for i in range(7):
	
	listInput = result['results'][i]['result']['tag']['classes']
	for i in range(len(listInput)-1):
		if listInput[i] != 'no person':
			finalWordList.append(listInput[i])
	
	wordList.append(finalWordList)
	
haikuWords1 = wordList[0]
haikuWords2 = wordList[1]
haikuWords3 = wordList[2]
haikuWords4 = wordList[3]
haikuWords5 = wordList[4]
haikuWords6 = wordList[5]
haikuWords7 = wordList[6]

myHaiku = haikuWords1[randint(0, len(haikuWords1) - 1)] + " " + haikuWords2[randint(0, len(haikuWords2) - 1)] + ", \n"
myHaiku += haikuWords3[randint(0, len(haikuWords3) - 1)] + " " + haikuWords4[randint(0, len(haikuWords4)-1)] + " " + haikuWords5[randint(0, len(haikuWords5) - 1)] + ", \n"
myHaiku += haikuWords6[randint(0, len(haikuWords6) - 1)] + " " + haikuWords7[randint(0, len(haikuWords7) - 1)] + ", \n"


print(myHaiku)








