from PIL import Image 
import pickle

import numpy as np 
from torch import Tensor

from model import Model

model_path = r".\model_weight\model.pickle"

def predict(image_path: str):
    image = Image.open(image_path)
    image = image.convert("RGB")
    image = image.resize((200, 200))

    with open(model_path, "br") as f:
        model: Model = pickle.load(f)

    X = Tensor(np.array(image)).reshape((1, 3, 200, 200))
    Y = model.predict(X)
    return Y.argmax(1)

if __name__ == "__main__":
    res = predict(r".\prepared_data\0000.png")
    print(res[0])
    
    