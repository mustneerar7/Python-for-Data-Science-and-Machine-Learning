import numpy as np
from tensorflow import keras

from tensorflow.keras.preprocessing import image

def getResults(provided_model):

    provided_image = input("Enter filename ie. [filename.jpg]: ")
    
    # loads compiled cnn into memory
    reconstructed_model = keras.models.load_model(provided_model)
    reconstructed_model.summary()
    
    # loads and resizes the provided image
    test_image = image.load_img(provided_image, target_size=(64, 64))
    
    # converts provided image to array
    test_image = image.img_to_array(test_image)
    
    # adds an extra dimension to array
    test_image = np.expand_dims(test_image, axis = 0)
    
    # uses the model to get results
    result = reconstructed_model.predict(test_image)
    
    if [0.] in result:
        print("its a cat")
    if [1.] in result:
        print('its a dog')

# moment of truth
getResults('cats_and_dogs')
