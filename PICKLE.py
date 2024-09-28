import pickle


data = {"name": "Alice", "age": 30, "occupation": "Engineer"}

with open("data.pickle", "wb") as file:
    # Pickle the Python object and save it to file
    pickle.dump(data, file)
print("Data has been serialized and saved to data.pickle")

with open("data.pickle", "rb") as file:
    loaded_data = pickle.load(file)
print("Deserialized data:", loaded_data)



