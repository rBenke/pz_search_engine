import pickle
import faiss
import numpy as np
class Search_engine:
    def __init__(self):
        with open("/app/item_embeddings.pickle", "rb") as file:
            data = pickle.load(file)
        d = "TODO: get data dimentionality"
        self.index = faiss.IndexFlatIP(d) # creates empty index
        self.index.add(data) # fill index with the data

    def search(self, vector):
        distance, best_fit = self.index.search(vector, 10) # search for 10 closest vectors in the index for 'vector'
        return best_fit
