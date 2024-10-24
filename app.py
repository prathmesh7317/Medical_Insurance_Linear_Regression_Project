# We create app.py, To check user input throgh POSTMAN API's...(Go te  Body>form-data>POSTm method select)
##[Note:- Create app.py outside Project Folder.]
### [Note: In Project Folder (only pkl,json,model.ipynb,& User-Test file,) & Outside Project Folder(config.py & app.py)]

## installation in env:-
# pip install pandas
# pip install Flask
# pip install scikit-learn
from flask import Flask,request,jsonify
import config
from Healthcare_Project.utils import MedicalInsurance  #in Healthcare_Project>utils.py(In this file, class is -MedicalInsurance)

app = Flask(__name__)

@app.route("/")  #'/' Home API
def get_home():
    return 'Home API'

@app.route("/Predict_Charges",methods = ['POST','GET']) #API Name:'/Predict_Charges
def get_medical():
    if request.method == 'POST':
        data = request.form  #form-data(input) through POSTMAN that is stored in variable 'data'
        age = data['age']
        bmi = data['bmi']
        children = data['children']
        smoker = data['smoker']
        region = data['region']

        obj = MedicalInsurance(age,bmi,children,smoker,region)  #Create object of class & gives set __init__ parameters from above(POSTMAN)
        Charges = obj.get_charges()  #Store in Charges becoz it returns a Number..

        return jsonify({"Result":f'Predicted medical insurance charges is {Charges}'})
    
if __name__ == '__main__':
    app.run()