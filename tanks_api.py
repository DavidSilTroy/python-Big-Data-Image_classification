from fastapi import FastAPI, UploadFile
from starlette.responses import RedirectResponse
from typing import Union
import pathlib
from PIL import Image
from io import BytesIO, StringIO

from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.all import *

app = FastAPI()

@app.get("/") #Redirecting to the fastai interface to check the methods
async def root():
    response = RedirectResponse(url='/docs#/default/create_upload_file_uploadfile__post')
    return response

@app.get("/api") #Just friendly greetings
async def root():
    return {"message": "Hello! you have to send a picture of your tank xd"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    image = read_image(await file.read()) #transforming the file in a fastai image
    return predict_tank(image) #Getting the prediction



def read_image(file: bytes) -> PILImage:
    img = Image.open(BytesIO(file))
    fastimg = PILImage.create(np.array(img.convert('RGB')))
    return fastimg

def predict_tank(image) -> Dict:
    model_name='tanks.pkl' #in case the model is moved to a folder -> 'folder/tanks.pkl'

    plt = platform.system()
    if plt == 'Windows': pathlib.PosixPath = pathlib.WindowsPath

    model = load_learner(pathlib.Path()/model_name)
    pred, pred_idx, probs = model.predict(image)
    prediction = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'
    return {
        "Prediction": prediction   
    }
    
