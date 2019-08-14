##load model and predict on cat
#Soroush H July 2019
import warnings
warnings.filterwarnings("ignore")
import numpy
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import xception

#cat pic import####################

#get picture the proper size for xception
kittyPic = image.load_img('chartreux.jpg', target_size=(299,299))
x = xception.preprocess_input(np.expand_dims(kittyPic.copy(), axis=0))

#cat names the way the model learned it
catNames = ["Bengal","Abyssinian","Birman","British Shorthair","Sphynx","Bombay","Persian","Ragdoll","Siamese","Russian Blue","Maine Coon","Egyptian Mau","Devon Rex","Manx","American Bobtail","American Curl","Cornish Rex","Don Sphynx","Khao Manee","Pixiebob","Japanese Bobtail","Chartreux","Tabby","Burmese","Somali","Tonkinese","Exotic Shorthair","Burmilla","Minskin","Savannah","Nebelung","Singapura","Havana","Oriental Longhair","Oriental Shorthair","Korat","Kurilian Bobtail","American Shorthair","Turkish Angora","Scottish Fold","Lykoi","Balinese","Peterbald","Scottish Fold LongHair","Selkirk Rex","Chausie","Munchkin","Ocicat","British Longhair","SnowShoe","Turkish Van","Siberian","Australian Mist","Toybob","LaPerm","Himalayan","Norwegian Forest Cat","American Wirehair"]

# get model
model = load_model('xceptionNewAug12.h5')
prediction = (model.predict(x))


labelList = np.argsort(-prediction, axis=1)   #get 5 most likely predictions
firstP = str(catNames[(labelList[0][0])])
secondP =  str(catNames[(labelList[0][1])])
third = str(catNames[(labelList[0][2])])
fourth = str(catNames[(labelList[0][3])])

#print("\n")
#print("I believe your cat is a " , end = '')
#print(catNames[label], end = '')
#print(" cat!")
#print("\n")


if (firstP == "Bengal"):
  print('Wow, if I had to guess, it looks like a Bengal cat!')
  print('It\'s a rare hybrid of the Asian Leopard and Egyptian Mau!')
  print('I also see similarities with these three other cats: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Abyssinian"):
  print('Looks to me like a Abyssinian! They\'re an Ethopian breed.')
  print('I also see similarities with these three other cats: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Birman"):
  print('Looks like a Birman! They\'re a sacred cat from Myanmar.')
  print('They share features with Balinese, Ragdoll\'s, Siamese, SnowShoe\'s, Tonkinese, Burmese and even Himalayan cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "British Shorthair"):
  print('Ooh, a European cat? Looks very similar to a British Shorthair to me.')
  print('They resemble a few other cats, namely the Chartreux of France, Russian Blue, and even the Korat of Thailand!')
  print('\nYours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Sphynx"):
  print('A type of Sphynx? Nay, that is a Sphynx! These naked fellas come from Toronto, where they bred cats with a mutation which resulted in no hair.')
  print('There are other types of Sphynx of course. It could be a Don Sphynx, or even a Peterbald!')
  print('Your cat shares the most similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Bombay"):
  print('Looks like a Bombay! They are made from combining Burmese with black American Short hairs.')
  print('Your cat also shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Persian"):
  print('Looks like a Gorgeous Persian! They were developped in the UK using, you guessed it, Turkish Cats.')
  print('They share very close similarities with, and the pure whites are often mistaken for, Maine Coons and even Persian cats.')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Ragdoll"):
  print('Looks like a Ragdoll! They were made in the 1960s in California.')
  print('They share features with Balinese, Birman\'s, Siamese, SnowShoe\'s, Tonkinese, Burmese and even Himalayan cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Siamese"):
  print('Looks like a Siamese! One of the many cats native to Thailand, and a very popular breed too!.')
  print('They share features with Balinese, Birman\'s, Ragdoll\'s, SnowShoe\'s, Tonkinese, Burmese and even Himalayan cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Russian Blue"):
  print('Ooh, a European cat? Looks very similar to a Russian Blue to me..')
  print('They resemble a few other cats, namely the Chartreux of France, the British Shorthair, and even the Korat of Thailand!')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Maine Coon"):
  print('Wow, if it\'s as large as it looks, that looks like a Maine Coon! It\'s the largest and oldest domesticated breeds in North America.')
  print('They share very close similarities with both the Norwegian Forest cat, as well as the Siberian. Some even resemble Persians.')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Egyptian Mau"):
  print('Meow, that\'s an Egyptian Mau. From Egypt as the name implies.')
  print('They are one of the few naturally spotted cat breeds, and are quite rare.')
  print('Yours also shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Devon Rex"):
  print('A Rex! Looks like a Devon Rex.')
  print('They look like Cornish Rex cats but with smaller snouts!')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Manx"):
  print('Oh wow a bobtail cat! This is one without bobtail in its name. It has a naturally occuring mutation that shortens its tail. They originate from the Isle of Man.')
  print('They naturally share similarities with other \'bob\' style cats, namely the Japanese Bobtail, the American Bobtail, the Kirilian Bobtail, the Pixie-bob and the Toybob')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "American Bobtail"):
  print('Oh wow a bobtail cat! This one looks like a American Bobtail. These bob cats originate from the USA as the name implies.')
  print('They naturally share similarities with other \'bob\' style cats, namely the Kurilian Bobtail, the Pixie-bob, the Toybob, the Japanese Bobtail and the Manx.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "American Curl"):
  print('Folded ears? Looks like a American curl to me. Unlike the Scottish Fold, these originate from the USA.')
  print('They also have a short hair variety, and also can resemble the American curl which also has curled ears.')
  print('Your cat shares the most similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Cornish Rex"):
  print('A Rex! Looks like a Cornish Rex at that.')
  print('They look like Devon Rex cats but with long Roman noses!')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Don Sphynx"):
  print('A type of Sphynx? Looks like a Don Sphynx! Also called the Russian Hairless. These naked fellas come from Russia.')
  print('There are other types of Sphynx of course. It could be a basic Sphynx, or even a Peterbald!')
  print('Your cat shares the most similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Khao Manee"):
  print('Those eyes though! That\'s KhaoManee to meee.')
  print('A very rare breed from Thailand, also called the Diamond eye. Its eyes can be blue, yellowish green, or one of each!')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)



elif(firstP == "Pixie-bob"):
  print('Oh wow a bobtail cat! This one looks like a Pixie-bob. These bob cats originate from the USA.')
  print('They naturally share similarities with other \'bob\' style cats, namely the Kurilian Bobtail, the American Bobtail, the Toybob, the Japanese Bobtail and the Manx.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Japanese Bobtail"):
  print('Oh wow a bobtail cat! This one looks like a Japanese Bobtail. They\'re native to both Japan and southeast Asia.')
  print('They naturally share similarities with other \'bob\' style cats, namely the Kurilian Bobtail, the American Bobtail, the Toybob, the Pixie-bob and the Manx.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Chartreux"):
  print('Ooh, a European cat? Looks very similar to a Chartreux to me..')
  print('They resemble a few other cats, namely the Russian Blue, the British Shorthair, and even the Korat of Thailand!')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Tabby"):
  print('Looks like your usual domestic cat, aka Tabby cat! Hard to pinpoint anything as it\'s generally a mix of many cats.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Burmese"):
  print('Looks like a Burmese! Originating as  cat from Thailand, which was later cross bread with American or British Shorthairs!')
  print('They share features with Balinese, Birman\'s, Siamese, SnowShoe\'s, Tonkinese, Ragdoll\'s and even Himalayan cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Somali"):
  print('Lovely shaded cat. This looks like a Somali. Unlike their name suggests, their origin as actually the United States.')
  print('They resemble Abyssinians as they\'re the product of a recessive gene in them.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Tonkinese"):
  print('Looks like a Tonkinese! These are made by breeding Siamese and Burmese cats!')
  print('They share features with Balinese, Birman\'s, Burmese, Siamese, SnowShoe\'s, Ragdoll\'s and even Himalayan cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Exotic Shorthair"):
  print('Those eyes though! Looks like a Exotic Shorthair.')
  print('These are developped to be short haired Persians, so they naturally share many similarities.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Burmilla"):
  print('Looks like a Burmilla. These were a cross between Chincilla Persians and the Burmese cats.')
  print('They resemble Burmese quite a bit as a result.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Minskin"):
  print('Is that kitty little? If so that looks like a Minskin. They are bred from mixing Munchkins with the Sphynx.')
  print('Of course, if it\'s just a smaller cat if could also just be a type of Sphynx, such as the Don Sphynx.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Savannah"):
  print('Is that a Cheetah? Looks like a Savannah cat!')
  print('They are a cross breed between a serval and a domestic cat')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Nebelung"):
  print('Tall, dark and Handsome. This looks like a Nebelung. A very rare breed from the US!')
  print('They are a semi-long haired Russian Blue in origins.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Singapura"):
  print('A cute from Singapore, aka a Singapura.')
  print('These cats are what happens when the US sends cats to Singapore, then gets them back a while later.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Havana"):
  print('Not Cuban, but Havana! A Havana Brown looks like. These are a result of breeding Siamese and black cats.')
  print('They originate from the UK.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Oriental Longhair"):
  print('Looks like an Oriential, long hair variety in this case..')
  print('Also referred to as the Mandarin or Foreign Longhair.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Oriental Shorthair"):
  print('Is that a Rex? Or a Siamese? Nope, looks like a Oriental Shorhair to me.')
  print('It has Siamese origins, which is where the simlaraties may come from. There\'s also a longhair variety.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == 'Korat'):
  print('Hmm, looks like a Korat to me...')
  print('They\'re from Thailand, but resemble a few Europeans cats, namely the Russian Blue, the British Shorthair, and the Chartreux of France!')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Kurilian Bobtail"):
  print('Oh wow a bobtail cat! This one looks like a Kurilian Bobtail. They originate from the Kuril Islands, as well as Russia')
  print('They naturally share similarities with other \'bob\' style cats, namely the Japanese Bobtail, the American Bobtail, the Toybob, the Pixie-bob and the Manx')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "American Shorthair"):
  print('An American Shorthair! These fellas originated from back when cats were brought from Europe on ships to deal with mice. A very popular cat.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Turkish Angora"):
  print('Looks like a beautiful Turkish Angora! One of the most ancient breeds from the Ankara region of Turkey.')
  print('They share very close similarities with, and are often mistaken for, Maine Coons and even Persian cats.')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Scottish Fold"):
  print('Folded ears? Looks like a Scottish Fold to me. As the name says, they originate from Scotland.')
  print('They have both a short and long hair variety, and also can resemble the American curl which also has curled ears.')
  print('Your cat shares the most similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Lykoi"):
  print('Is that a werewolf? Looks like a Lykoi cat!')
  print('Not to be confused with the Sphynx or Devon line. These originate from Tennesee.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Balinese"):
  print('Looks like a Balinese! An American Cat with a Siamese Ancestry.')
  print('They share features with Birman, Ragdoll\'s, Siamese, SnowShoe\'s, Tonkinese, Burmese and even Himalayan cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Peterbald"):
  print('A type of Sphynx? Nope, that looks like a Peterbald to me! Although it could also be a Sphynx or a Russian Hairless as well. These guys were made through experimentation in St. Petersburg.')
  print('Your cat shares the most similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Scottish Fold Longhair"):
  print('Folded ears and long hair? Looks like a Scottish Fold Longhair to me. As the name says, they originate from Scotland.')
  print('They also have a short hair variety, and also can resemble the American curl which also has curled ears.')
  print('Your cat shares the most similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Selkirk Rex"):
  print('A Rex! But not just any kind, looks like a Selkirk Rex.')
  print('Unlike the Devon and Cornish Rex, Selkirks have full normal hair. They also greatly resemble LaPerm cats!')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Chausie"):
  print('Looks like a Chausie. A larger Egyptian origina cat..')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Munchkin"):
  print('Who\'s that little guy? Looks like a Munchkin, also called a Sausage cat.')
  print('Yours specifically shares some similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "Ocicat"):
  print('Bengal? No that looks like an ocicat to me. Bred from mixing Siamese, Abyssinian and Tabby cats in the USA.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "British Longhair"):
  print('Longhair and round face, looks like a British Longhair.')
  print('They resemble persians a bit, and even Maine coons. They also have a shorter hair variety.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "SnowShoe"):
  print('Looks like a SnowShoe Cat! They\'re a sub species of Siamese cats originating from Philadelphia!')
  print('They share features with Balinese, Birman\'s, Siamese, Burmese, Tonkinese, Ragdoll\'s and even Himalayan cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Turkish Van"):
  print('Looks like a Turkish Van! They were developped in the UK using, you guessed it, Turkish Cats.')
  print('Your kitty also shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Siberian"):
  print('That wooly kitty looks to be a Siberian. Has been found in Russia for centuries now.')
  print('They share very close similarities with both the Maine Coon, as well as the Norwegian Forest Cat. Some even resemble Persians a bit.')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Australian Mist"):
  print('Simple and clean. This kitty looks like an Australian mist!')
  print('It has a lot of similar features to other cats, such as spots and the tabby cat look.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Toybob"):
  print('Oh wow a bobtail cat! This one looks like a Toybob. They originate from Russia')
  print('They naturally share similarities with other \'bob\' style cats, namely the Japanese Bobtail, the American Bobtail, the Kirilian Bobtail, the Pixie-bob and the Manx')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)


elif(firstP == "LaPerm"):
  print('Looks like a curly LaPerm. They originate from the US, but are common to find everywhere now.')
  print('They look very similar to Selkirk Rex cat!')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Himalayan"):
  print('Looks like a Himalayan Cat! They\'re a mix of Siamese and Persian cats!')
  print('They share features with Balinese, Birman\'s, Siamese, SnowShoe\'s, Tonkinese, Ragdoll\'s and even Burmese cats!')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "Norwegian Forest Cat"):
  print('Quite the coat! Your cat resemebles a Norwegian Forest cat! Has a warm coat for the cold weather up in Norway.')
  print('They share very close similarities with both the Maine Coon, as well as the Siberian. Some even resemble Persians a bit.')
  print('Yours specifically shares some similarities with these three: ')
  print (secondP)
  print (third)
  print (fourth)

elif(firstP == "American Wirehair"):
  print('Looks like an American Wirehair! They originate from the US and are caused by a mutation found in the American Shorthair.')
  print('So they naturally resemble the American Shorthair.')
  print('Yours specifically shares some great similarities with these three breeds: ')
  print (secondP)
  print (third)
  print (fourth)






	

