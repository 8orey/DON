from dataset_preparation import preparation 
from dataset_prepreparation import prepreparation 

def all_prepare():
    from sys import argv

    params = argv[1:]

    if "-pp" not in params:
        prepreparation()
    if "-p" not in params:
        preparation()

if __name__ == "__main__":
    all_prepare()
