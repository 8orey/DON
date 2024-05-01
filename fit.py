import pandas as pd 
import numpy as np 
import torch as th
from PIL import Image

from model import Model

amount = 3

def fit():

    csv = pd.read_csv(r".\data\dataset.csv")

    paths = list(csv["path"])[:amount]
    print(paths)

    pict = np.array([np.array(Image.open(path)) for path in paths])
    print("Pict loaded")

    # print(pict.shape)
    # return 

    X = th.Tensor(pict).reshape((-1, 3, 200, 200))
    print("X transformed")

    Y = th.Tensor([list(row)[1:] for row in csv.iloc][:amount])

    print(Y.shape)

    model = Model()
    model.fit(X, Y)
    model.save(r"./model_weight/model.pickle")








if __name__ == "__main__":
    fit()


