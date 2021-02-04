import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os
import cv2
import keras
from keras.models import Sequential
from keras.layers import Conv2D,Dense,MaxPooling2D,Flatten,BatchNormalization,AveragePooling2D
from keras.applications.vgg16 import VGG16

st.title('Mechanical parts detection')
st.write("We will try to classify the mechanical parts with our Deep Learning model: ")

# Adding model
vgg_model = VGG16(input_shape=(128,128,3),include_top=False,weights='imagenet')
model = Sequential()
model.add(vgg_model)
model.add(Flatten())
model.add(Dense(4,activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer=keras.optimizers.Adam(lr=1e-3), metrics=['accuracy'])
#Load the weights of the model trained on colab
model.load_weights('model.h5')

# Defining a function that tests on a custom image using image
# First we identify the actual class labels and what their corresponding index in the model
labels = {'bolt': 0, 'locatingpin': 1, 'nut': 2, 'washer': 3}
labels = dict((v,k) for k,v in labels.items())

def mechanical_parts_predictor(image):
  resized_test = cv2.resize(image,(128,128))
  list_of_test_images = []
  list_of_test_images.append(resized_test)
  test_image = np.array(list_of_test_images)
  prediction = model.predict_generator(test_image)
  st.write(prediction)
  if (max(prediction[0])<0.9):
    return "not of any known mechanical part"
  predicted_class_index = np.argmax(prediction)
  return labels[predicted_class_index]

st.title("Upload your file")
uploaded_file = st.file_uploader("Choose an image...", accept_multiple_files=False, type=['png','jpg'])
st.write(uploaded_file)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.asarray(image)
    if len(image.shape) == 2:
      new_image = np.zeros((image.shape[0],image.shape[1],3))
      for ch in range(3):
        for x in range(image.shape[0]):
          for y in range(image.shape[1]):
            new_image[x,y,ch] = image[x,y]
    elif image.shape[2] == 4:
      new_image = image[:,:,:3]
    else:
      new_image = image
    st.image(uploaded_file, caption='Uploaded Image.',use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = mechanical_parts_predictor(new_image)
    st.write("The given image is of "+ label)
