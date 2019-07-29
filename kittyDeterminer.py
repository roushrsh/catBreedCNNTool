##load model and predict on cat
#Soroush H July 2019

import numpy
import tensorflow as tf
import os
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import load_img
from keras.models import load_model
from keras.applications import xception

#cat pic import####################

#get picture the proper size for xception
kittyPic = image.load_img('persian.jpg', target_size=(299,299))
x = xception.preprocess_input(np.expand_dims(kittyPic.copy(), axis=0))


#cat names the way the model learned it
catNames = ["Bengal","Abyssinian","BritishShorthair","Birman","Sphynx","Bombay","EgyptianMau","Persian","Ragdoll","MaineCoon","Siamese","RussianBlue","AmericanBobtail","DevonRex","AmericanCurl","DonSphynx","Manx","Balinese","Burmilla","Burmese","KhaoManee","Chausie","AmericanShortHair","Chartreux","Pixiebob","JapaneseBobtail","BritishLonghair","CornishRex","Tabby","Somali","ExoticShortHair","Tonkinese","OrientalShortHair","Minskin","Korat","Savannah","Havana","Singapura","Nebelung","OrientalLonghair","TurkishAngora","ScottishFold","KurilianBobtail","Lykoi","ScottishFoldLonghair","Ocicat","Munchkin","SelkirkRex","AustralianMist","AmericanWireHair","TurkishVan","SnowShoe","Peterbald","Siberian","Toybob","Himalayan","LePerm","NorwegianForestCat"]



# get model
model = load_model('RoushKitty70Model.h5')
prediction = (model.predict(x))


#print(prediction)


label = int(np.argmax(prediction, axis=-1))    
#print(labels)
print("\n")
print("I believe your cat is a " , end = '')
print(catNames[label], end = '')
print(" cat!")
print("\n")


