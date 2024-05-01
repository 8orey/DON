from glob import glob 
import pandas 

def prepreparation():
    nation = []
    path = r".\dataset\*"
    for country in glob(path):
        name = country[len(path)-1:]
        nation.append(name)

    raw_data: dict[str, list[str]] = {
        "path": [],
        "nation": []
    }

    for country in nation:
        path = fr".\dataset\{country}\*"
        for file_name in glob(path):
            raw_data["path"].append(file_name)
            raw_data["nation"].append(country)
    
    dataset = pandas.DataFrame(raw_data)

    dataset.set_index("path", inplace=True)

    dataset.to_csv(r"./preprepared_data/dataset.csv")

if __name__ == "__main__":
    prepreparation()
