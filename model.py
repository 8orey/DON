from torch.nn import *

from tqdm import tqdm 

import torch 

from torch import Tensor, tensor, float64  

from PIL import Image 

from dataset_preparation import count_countries

from torch.optim import SGD

import pickle

class Model:
    model: Sequential  
    def __init__(self) -> None:
        self.model = Sequential(
            Conv2d(3, 10, (51, 51)),
            Tanh(),

            Conv2d(10, 10, (36, 36)),
            Tanh(),

            Flatten(1),
            Linear(132250, count_countries),

            Softmax(1)
        )
    
    def predict(self, imgs: Tensor) -> Tensor:
        with torch.no_grad():
            return self.model(imgs)
    
    def fit(self, imgs: Tensor, Y: Tensor) -> None:
        epochs = 5
        rate = 1/1e1

        loss_fn = MSELoss()
        optimizer = SGD(params=self.model.parameters(), lr=rate)
        
        for t in tqdm(range(epochs)):
            y_pred = self.model(imgs)
            loss = loss_fn(y_pred, Y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        print(loss.item())
    
    def save(self, path: str):
        file = open(path, 'bw')
        pickle.dump(self, file)


    
    






