import streamlit as st
import pathlib
from PIL import Image
from io import BytesIO, StringIO

from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.all import *


@st.experimental_memo
def get_categories(_model):
    return _model.dls.vocab


def showcase():
    st.header('Thomas More - Big Data Team Assigment: Image Classification')
    st.subheader('War Tanks Classification')

    model_name='tanks.pkl'

    plt = platform.system()
    if plt == 'Windows': pathlib.PosixPath = pathlib.WindowsPath
    model = load_learner(pathlib.Path()/model_name)

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

