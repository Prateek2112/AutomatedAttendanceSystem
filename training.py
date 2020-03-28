#Importing Required Libraries

from tensorflow.keras.layers import Input, Dense, Dropout, Conv2D, MaxPool2D, BatchNormalization, Flatten
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG19, ResNet50
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import Model

import tensorflow.keras.backend as K
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os, re, cv2
import itertools

#Defining the model objects for ResNet50 and VGG19

K.clear_session()
base_model = ResNet50(include_top=False, weights='imagenet', input_shape=(32,32,3))
base_model_vgg = VGG19(include_top=False, weights='imagenet', input_shape=(32,32,3))

#Making the VGG19 Dense layers non-trainable

for layer in base_model_vgg.layers:
    layer.trainable= False

base_model_vgg.summary()

#Adding some customized layers for the model

y1 = base_model_vgg.output
y1 = Flatten()(y1)
y1 = BatchNormalization()(y1)
y1 = Dense(128,activation='relu')(y1)
y1 = Dropout(0.3)(y1)
y1 = BatchNormalization()(y1)
y1 = Dense(64, activation='relu')(y1)
y1 = Dropout(0.4)(y1)
y1 = Dense(26, activation='softmax')(y1)
model2 = Model(base_model_vgg.input, y1)
model2.summary()

#Image data generator for training

image_data_generator = ImageDataGenerator(rescale = 1./255, rotation_range = 20, 
                                          vertical_flip=True, horizontal_flip=True)

#Image data generator for validating

image_data_generator1 = ImageDataGenerator(rescale = 1./255)

train_generator = image_data_generator.flow_from_directory('/content/resizedtrain/faces', 
                                                           class_mode = 'categorical',batch_size = 32,
                                                           target_size = (32,32))

validation_generator = image_data_generator1.flow_from_directory("/content/resizedval", 
                                                                 class_mode='categorical', 
                                                                 batch_size = 32, 
                                                                 target_size = (32,32))

es = EarlyStopping(monitor='val_loss', patience=10)
rlr= ReduceLROnPlateau(factor=0.5) #change values
chk_pts = ModelCheckpoint(monitor='val_loss', save_best_only=True, filepath='best_model.h5')

model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
history=model2.fit_generator(generator=train_generator,validation_data=validation_generator,
                             validation_steps=32, steps_per_epoch=64, epochs=30, 
                             callbacks=[rlr,chk_pts]) #more no of epochs

model_json = model2.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model2.save_weights("model.h5")
print("Saved model to disk")

model2.save('face.model')



#Plotting the Train and Validation Losses

import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plt.subplot(1, 2, 1)
plt.suptitle('Optimizer : Adam', fontsize=10)
plt.ylabel('Loss', fontsize=16)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend(loc='upper right')

plt.subplot(1, 2, 2)
plt.ylabel('Accuracy', fontsize=16)
plt.plot(history.history['acc'], label='Training Accuracy')
plt.plot(history.history['val_acc'], label='Validation Accuracy')
plt.legend(loc='lower right')
plt.show()

predictions = model2.predict_generator(generator=validation_generator)
y_pred = [np.argmax(probas) for probas in predictions]
y_test = validation_generator.classes
class_names = validation_generator.class_indices.keys()

#Plotting the confusion matrix

def plot_confusion_matrix(cm, classes, title='Confusion matrix', cmap=plt.cm.Blues):
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.figure(figsize=(15,15))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    
# compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

# plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, title='Normalized confusion matrix')
plt.show()