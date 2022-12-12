import streamlit as st
import pathlib
from PIL import Image
from io import BytesIO, StringIO

from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.all import *
import io
import requests
# import gdown


# Get the pkl file from Google Drive and cache it
@st.experimental_memo
def get_model():
    response = requests.get(
        # This link might break at any time (is the direct download link extracted from the download form post)
        # Workaround the 100mb GitHub limit without using LFS with its stupid 1gb bandwidth limit
        'https://drive.google.com/uc?export=view&id=1-apihmCjwU5QnQburu_70UAUMDs0l1RP&confirm=t&uuid=0f357a46-916e-4b38-a46c-92621c4ada1d&at=AHV7M3fTmc_oRVxFTJknxIr9MLbx:1670871542558')
    model = io.BytesIO(response.content)
    return model


def googledrive():
    st.header('Thomas More - Big Data Team Assigment: Image Classification')
    st.subheader('War Tanks Classification - Google Drive storage')

    # id = "1-apihmCjwU5QnQburu_70UAUMDs0l1RP"
    # output = "export.pkl"
    # gdown.download(id=id, output=output, quiet=False)

    model_pkl = get_model()
    model = load_learner(model_pkl)

    image = st.file_uploader("Upload file", type=["png", "jpg", "jpeg"])
    show_image = st.empty()

    if not image:
        show_image.info("Choose a file to upload, only type: png, jpg, jpeg ")
        return
    else:
        image = PILImage.create((image))
        show_image.image(image.to_thumb(500, 500), caption='Uploaded Image')

    if st.button('Classify'):
        pred, pred_idx, probs = model.predict(image)
        st.write(f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}')
        # st.write(f'Prediction: {model.predict(image)}')
    else:
        st.write(f'Click the button to classify')

    image.close()
