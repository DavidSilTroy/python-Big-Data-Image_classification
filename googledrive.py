import streamlit as st
import pathlib
from PIL import Image
from io import BytesIO, StringIO
import pandas as pd
import numpy as np

from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.all import *
import io
import requests


# Get the pkl file from Google Drive and cache it
@st.experimental_memo
def get_model():
    response = requests.get(
        # This link might break at any time (is the direct download link extracted from the download form post)
        # Workaround the 100mb GitHub limit without using LFS with its stupid 1gb bandwidth limit
        'https://drive.google.com/uc?export=view&id=1-apihmCjwU5QnQburu_70UAUMDs0l1RP&confirm=t&uuid=0f357a46-916e-4b38-a46c-92621c4ada1d&at=AHV7M3fTmc_oRVxFTJknxIr9MLbx:1670871542558')
    model = io.BytesIO(response.content)
    return model


@st.experimental_memo
def get_categories(_model):
    return _model.dls.vocab


def googledrive():
    st.header('Thomas More - Big Data Team Assigment: Image Classification')
    st.subheader('War Tanks Classification - Google Drive storage')

    model_pkl = get_model()
    model = load_learner(model_pkl)

    if st.button("Clear cache and redownload model", help="Useful when the cached model is older than the one on Google Drive"):
        # Clear get_model's memoized values:
        get_model.clear()
        model_pkl = get_model()
        model = load_learner(model_pkl)

    image = st.file_uploader("Upload file", type=["png", "jpg", "jpeg", "webp"])
    show_image = st.empty()

    if not image:
        show_image.info("Choose a file to upload, only type: png, jpg, jpeg, webp ")
        return
    else:
        image = PILImage.create((image))
        show_image.image(image.to_thumb(500, 500), caption='Uploaded Image')

    if st.button('Classify'):
        pred, pred_idx, probs = model.predict(image)
        st.write(f'Prediction: {pred}; Probability: {probs[pred_idx]*100:.02f}%')

        chart_data = pd.DataFrame({'Probability (%)': probs*100}, index=get_categories(model))
        st.bar_chart(chart_data)
    else:
        st.write(f'Click the button to classify')

    image.close()
