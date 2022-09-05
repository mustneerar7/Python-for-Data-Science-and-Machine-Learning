from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# initialization - creating sequential model
cnn = Sequential()

# convolution - adding filters
cnn.add(Convolution2D(
    filters=32, kernel_size=3, padding='same', activation='relu'
    )
)
# adding second convolutional layer
cnn.add(Convolution2D(
    filters=64, kernel_size=3, padding='same', activation='relu'
    )
)

# pooling - reducing file dimensions
cnn.add(MaxPool2D(pool_size=(2,2)))

# flattening - converting pooled layer into
# single input layer
cnn.add(Flatten())

# full connection - a usual ann
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=1, activation='sigmoid'))

cnn.compile(
    optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']
)

# generating datasets from files
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

# creating training set
train_set = train_datagen.flow_from_directory(
        'pet_images/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

# creating test set
test_set = test_datagen.flow_from_directory(
        'pet_images/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

# fitting datasets on cnn
cnn.fit(
        train_set,
        steps_per_epoch=334,
        epochs=25,
        validation_data=test_set,
        validation_steps=334)

# saving the trained model for future use
model_name = 'cats_and_dogs'
cnn.save(model_name)
