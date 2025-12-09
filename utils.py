import streamlit as st
import numpy as np
import tensorflow as tf
from keras.applications.resnet import preprocess_input
from PIL import Image
from keras.models import Model
from keras.layers import GlobalAveragePooling2D
import pickle


def class_lables():
    labels = ['ADI', 'BACK', 'DEB', 'LYM', 'MUC', 'MUS', 'NORM', 'STR', 'TUM']
    labels.sort()
    return labels



def preprocess_img(sample_image, IMG_SIZE):
    base_model = tf.keras.applications.ConvNeXtXLarge(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    # Add average pooling to the base
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    model_frozen = Model(inputs=base_model.input,outputs=x)

    sample_image = Image.open(sample_image).convert("RGB")
    img_array = sample_image.resize(IMG_SIZE)
    img_batch = np.expand_dims(img_array, axis = 0) # Rows
    image_batch = img_batch.astype(np.float32)
    image_batch = preprocess_input(image_batch)
    prediction = model_frozen.predict(img_batch)
    return prediction


def load_model(model_name):
    file_name = open(model_name, "rb")
    return pickle.load(file_name)


def prediction(modelname, sample_image, IMG_SIZE=(224,224)):
    labels = class_lables()

    try:
        data_arr = preprocess_img(sample_image, IMG_SIZE)
        model = load_model(modelname)
        print(model)
        predictions = model.predict(data_arr)
        class_idx = predictions[0]
        return labels[class_idx]


    except Exception as e:
        st.write("ERROR: {}".format(str(e)))