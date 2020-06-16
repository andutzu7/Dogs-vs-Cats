# reduce the init dataset size
# use more keras
# search more types os labeling
# use the imahedatagenerator from keras
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(200, 200, 3)))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(64))
model.add(Dropout(0.5))
model.add(Dense(1))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.summary()

batch_size = 10

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(200, 200),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    'data/validation',
    target_size=(200, 200),
    batch_size=batch_size,
    class_mode='binary')

model.fit_generator(
        train_generator,
        steps_per_epoch=2974//batch_size,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=202//batch_size)
model.save_weights('nn.h5')
