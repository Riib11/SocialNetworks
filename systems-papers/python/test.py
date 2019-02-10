import pickle

x = {"hello":1}

with open("test.json", "wb+") as file:
    pickle.dump(x, file)

with open("test.json", "rb") as file:
    x = pickle.load(file)
    print(x)
