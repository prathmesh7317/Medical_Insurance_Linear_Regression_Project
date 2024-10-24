# In utils.py file, We read Pickle & JSON file to predit charges....
# Create utils.py file in Project folder, where we stored pkl_model & json_data files..``
### [Note: In Project Folder (only pkl,json,model.ipynb,& User-Test file,) & Outside Project Folder(config.py & app.py)]

import pickle
import json
import numpy as np  #in environment install- pip install numpy
import config

class MedicalInsurance():
    def __init__(self,age,bmi,children,smoker,region):  # __init__ used to set parameters....
        self.age = age
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
    def load_model(self):  #in "load_model" we stored pickle & json file as read..
        with open(config.pickle_model_path,"rb") as file:
            self.pkl_model = pickle.load(file) 
        with open(config.json_path,"r") as file:
            self.data_json = json.load(file)
    def get_charges(self):
        self.load_model()   # we are calling model, because want to use instance variable(self.data_json) of that "load_model" function..so
        test_array = np.zeros(len(self.data_json['columns'])) #We use instance variable o data_json...& By DEFAULT "float" for bmi
        test_array[0] = self.age    #test_array = array([0,0,0,0,0])
        test_array[1] = self.bmi
        test_array[2] = self.children
        test_array[3] = self.data_json['smoker'][self.smoker] # 'no':0,'yes':1
        test_array[4] = self.data_json['region'][self.region] # 'region': {'southeast': 1, 'southwest': 2, 'northwest': 3, 'northeast': 4}

        predict_charges = np.around(self.pkl_model.predict([test_array])[0],2)  #We have to pass 2D array for Model
        return predict_charges                                        #[0] used ,becoz it is in array so we waanna show output as values so array[0]
    
        







