from keras.models import load_model
import keras
classifier = load_model('TRAINED_INDIAN_DATA_FINAL_MODEL.h5')
# classifier.evaluate()

#Prediction of single image
import numpy as np
from keras.preprocessing import image
image_path = input('Enter Image Name: ')
# image_path = './predicting_data/{}'.format(img_name)
print('')

test_image = keras.utils.load_img(image_path, target_size=(128, 128))
test_image = keras.utils.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
#training_set.class_indices
print('Predicted Sign is:')
print(result)

if result[0][0] == 1:
       print("1")
elif result[0][1] == 1:
       print ('2')
elif result[0][2] == 1:
       print ('3')
elif result[0][3] == 1:
       print ('4')
elif result[0][4] == 1:
       print ('5')
elif result[0][5] == 1:
       print ('6')
elif result[0][6] == 1:
       print ('7')
elif result[0][7] == 1:
       print ('8')
elif result[0][8] == 1:
       print ('9')
elif result[0][9] == 1:
       print ('A')
elif result[0][10] == 1:
       print ('B')
elif result[0][11] == 1:
       print ('C')
elif result[0][12] == 1:
       print ('D')
elif result[0][13] == 1:
       print ('E')
elif result[0][14] == 1:
       print ('F')
elif result[0][15] == 1:
       print ('G')
elif result[0][16] == 1:
       print ('H')
elif result[0][17] == 1:
       print ('I')
elif result[0][18] == 1:
       print ('J')
elif result[0][19] == 1:
       print ('K')
elif result[0][20] == 1:
       print ('L')
elif result[0][21] == 1:
       print ('M')
elif result[0][22] == 1:
       print ('N')
elif result[0][23] == 1:
       print ('O')
elif result[0][24] == 1:
       print ('P')
elif result[0][25] == 1:
       print ('Q')
elif result[0][26] == 1:
       print ('R')
elif result[0][27] == 1:
       print ('S')
elif result[0][28] == 1:
       print ('T')
elif result[0][29] == 1:
       print ('U')
elif result[0][30] == 1:
       print ('V')
elif result[0][31] == 1:
       print ('W')
elif result[0][32] == 1:
       print ('X')
elif result[0][33] == 1:
       print ('Y')
elif result[0][34] == 1:
       print ('Z')
else :
       print('not found')

