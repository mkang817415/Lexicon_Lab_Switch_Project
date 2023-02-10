import pymagnitude 
from pymagnitude import * 
from pymagnitude import MagnitudeUtils 
import pandas as pd 
import difflib as dl


class Switch: 
    
    def __init__(self, filename): 
        #self.df = dataframe for id, word, embeddings from the specific excel file
        self.name = filename 
        self.file = pd.read_excel(filename) 
        self.data_dict = {} 
        
        # extracts id and words from the file 
        original_words = self.file["spellcheck"].values.tolist() 
    
        words = self.file["spellcheck"].values.tolist()
        words = [x.lower() for x in words]
        words = [x.strip() for x in words]
        words = [x.replace(" ", "_") for x in words]
        words = [x.replace("-", "_") for x in words]
        
        id_list = self.file["subject"].values.tolist() 
        
        #creates an data_dict of Id as keys and words as values 
        idx = 0 
        while idx != len(id_list): 
            if id_list[idx] in self.data_dict.keys(): 
                self.data_dict[id_list[idx]] += [words[idx].replace(" ", "_")]
                idx += 1 
            else: 
                self.data_dict[id_list[idx]] = [words[idx].replace(" ", "_")]
                idx += 1
                
        # Creating list for if word has vector s
        vectors = Magnitude(MagnitudeUtils.download_model('word2vec/medium/GoogleNews-vectors-negative300'))
        self.df = pd.DataFrame()
        self.df["ID"] = id_list
        self.df["Original Words"] = self.file["spellcheck"].values.tolist()
        self.df["Words"] = words 
        self.df["Has Vectors"] = [x in vectors for x in words]
        
        embeddings = [] 
        for x in words: 
            vector = vectors.query(x) 
            vector = vector.tolist() 
            embeddings.append(vector[:49])
        # for x in words: 
        #     if x in vectors: 
        #         vector = vectors.query(x)
        #         vector = vector.tolist()
        #         embeddings.append(vector[:49])
        #     else: 
        #         embeddings.append("N/A")
        self.df["Embeddings"] = embeddings 
        


    def save_file(self, out_filename): 
        self.df.to_excel(out_filename) 
        



a = Switch("fovacs_animals.xlsx") 
a.save_file("animals_embedding.xlsx")

a = Switch("fovacs_cities.xlsx") 
a.save_file("cities_embedding.xlsx")

a = Switch("fovacs_foods.xlsx") 
a.save_file("foods_embedding.xlsx")

a = Switch("fovacs_occupations.xlsx") 
a.save_file("occupations_embedding.xlsx")

a = Switch("fovacs_sports.xlsx") 
a.save_file("sports_embedding.xlsx")

a = Switch("fovacs_vehicles.xlsx") 
a.save_file("vehicles_embedding.xlsx")




            

    