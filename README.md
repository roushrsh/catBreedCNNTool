Update 2:
V0.3  August 13 2019
Increased the validation to 75:25 and filtered through pictures again. Lots of duplicates and useless pictures were removed. New model with 91% validation, 98% training accuracy obtained. Under 1 in 10 is alright. Most are it calling Chartreux as British Shorthair as the google results for Chartreux are almost all British Shorthairs, and vice verca lots of cross contamination. This occurs for many breeds so the output in kittyDeterminerMain.py mentions similarities and also shows the 3 next closest cats the cat resembles.

---------------------
Update 1:
V0.2 After improving the learning results for some problem breeds and changing training parameters, accuracy of almost 94% is obtained on validation, nearly 98% on training.

---------------
V 0.1 
I am using an updated Xception model which was trained using imagenet weights.

Other models were tested such as Resnet50, InceptionV3, etc. but Xception was found to be the most accurate. 

Most of the effort went into accumulating and sorting the images. Currently around 5500 are used for 58 different breeds.

The breeds were chosen from official cat registeries such as "The cat fanciers' Association", "Fédération Internationale Féline", and others.

There are a lot of very similar looking breeds which are just slight variations of one another, so I plan on having the top 3 or so possible breeds appear for each result.

The code used is relatively simple, and available as a ipynb file.

After Xception was settled upon, I split the training into 80:20 for a validation set.

I use imageDataGenerator to augment the images with rotation, zoom, flip and shear to a small extent, to mimick the average person photography skills.

I currently only have access to a laptop 1050ti gpu so I used a small batch size. First a dense layer was pretrained to avoid a large gradient, at 40 epochs. This achieved an accuracy of 55% on the 58.

Next the entire Xception model was trained for another 110 epochs, and the learning rate was reduced after every 40 epochs. 
This achieved an accuracy of 70.05% on the validation set (94 % on training set).


Things which can be improved:

A lot of cat breeds look similar, having an expert go through them and sort them, and add more pictures would greatly improve results.
There are some breeds which are very similar looking (for example the bobtails, Himalayans/Siamese, Thai cats in general, Don Sphynx and Sphynx, Cornish Rex and Devon Rex, etc.)
If those breeds were grouped as just one general breed per group, results would undoubteably greatly improve.
