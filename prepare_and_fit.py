from fit import fit
from prepare import all_prepare 

def prepare_and_fit():
    all_prepare()
    fit()

if __name__ == "__main__":
    prepare_and_fit()