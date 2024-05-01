from PIL import Image
import pandas 

new_size = (200, 200)
count_countries = 7

def preparation():
    dt = pandas.read_csv(r".\preprepared_data\dataset.csv")

    index = 0

    place_path = r".\prepared_data\{:0>4}.png"

    paths = []

    new_dt = dt.copy(deep=True)

    for filename in dt.path:
        image = Image.open(filename)
        image = image.convert("RGB")
        image = image.resize(new_size)
        cur_place = place_path.format(index)

        try:
            image.save(cur_place, format="png")
            
            paths.append(cur_place)
        except:
            new_dt.drop([index])
        index += 1 

    indexes = {}
    for index, country in enumerate(new_dt.nation.unique()):
        indexes[country] = index 

    new_dt.path = pandas.DataFrame(paths)

    new_new_dt = []

    for path, cur in zip(new_dt.path, new_dt.nation):
        new_new_dt.append([path] + [0] * len(indexes))
        new_new_dt[-1][indexes[cur] + 1] = 1 

    dataframe = pandas.DataFrame(new_new_dt, columns=["path", *indexes.keys()])

    dataframe.set_index("path", inplace=True)

    dataframe.dropna()

    dataframe.to_csv(r".\data\dataset.csv") 

if __name__ == "__main__":
    preparation()
