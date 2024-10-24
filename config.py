## We create config.py file becoz, We have to stored Model(.pkl) & JSON file path in this file.....
# Create config.py file, Outside Project folder...becoz we have to store path..
### [Note: In Project Folder (only pkl,json,model.ipynb,& User-Test file,) & Outside Project Folder(config.py & app.py)]

import os

pickle_model_path = os.path.join('Healthcare_Project','Healthcare(env)_myproject.pkl')    # Healthcare_Project\Healthcare(env)_myproject.pkl..[relative path]
json_path = os.path.join('Healthcare_Project','json_Healthcare(env).json')                     # Healthcare_Project\json_Healthcare(env).json..[relative path]