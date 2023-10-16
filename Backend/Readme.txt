Assuming for the Backend-
Model is saved in a Pickle file- Named as "Saved_model.pkl"
And Classes for Classification are stored in "Class_Dictionary.json"

Code snippet to save Model in a Pickle file-
!pip install joblib
import joblib
#Saving the Model in a Pickle file
joblib.dump(ClassifierModel,"Saved_model.pkl")

Code snippet to save Classes in a Json file-
import json
with open("Class_Dictionary.json","w") as file:
    file.write(json.dumps(Class_Dict))

There is an ModelObjects Folder which stores-
Saved_model.pkl
Class_Dictionary.json

Folder Structure for Backend Work-
ModelObjects
    -Class_Dictionary.json
    -Saved_model.pkl
Readme.txt
Server.py
Utilities.py

The Only way I found to process Image for prediction was through encoding
The Image has to be converted to a Base64 string
The Base64 string will be stored in a File
So a Txt File will be passed for predictions
Website for the purpose-https://www.base64-image.de/
Contributor Kamalpreet Singh(21103029)