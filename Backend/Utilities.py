import json
import numpy as np
import base64
import cv2
import joblib

__class_name_to_number={}
__class_number_to_name={}
__model=None

def OpeningFile(filename):#Give Full File name-"Filename.txt"
    #The Filename is a string including the extension of the Text file
    with open(filename) as file:
        return file.read()
    
def Classify_Image(ImageBase64Data,filepath=None):
    #filepath-If we wish to directly give the path

    #Image Preprocessing-Done according to what was followed while Building the Model
    finalImage=""#Here it is jsut a PlaceHolder
    #Has to be Completed once the Model Building is completed

    result={}
    prediction=__model.predict(finalImage)[0]
    predictedClass=class_name_to_number(prediction)
    probabilityval=__model.predict_proba(finalImage)
    result.append({
        "class":predictedClass,
        "probability":np.round(probabilityval,2).tolist()[0],
        "class_Dictionary":__class_name_to_number#For UI Purposes to map the Classes to Images
        })
    return result

def class_number_to_name(classNumber):
    return __class_number_to_name[classNumber]

def class_name_to_number(className):
    return __class_name_to_number[className]

def load_saved_ModelObjects():
    print("Loading Model Objects-")
    global __class_name_to_number
    global __class_number_to_name

    with open("./ModelObjects/Class_Dictionary.json","r") as file:
        __class_name_to_number=json.load(file)
        __class_number_to_name={v:k for k,v in __class_name_to_number.items()}

    global __model
    if __model is None:
        with open("./ModelObjects/Saved_model.pkl","rb") as file1:
            __model=joblib.load(file1)
    print("Loading Model Objects Successful")

if __name__=="__main__":
    # filename=""
    # print(Classify_Image(Classify_Image(filename),None))
    load_saved_ModelObjects()

    #For Testing purposes
    print(Classify_Image(None,"./TestingData/Test_Image1.jpg"))
    print(Classify_Image(None,"./TestingData/Test_Image2.jpg"))
    print(Classify_Image(None,"./TestingData/Test_Image3.jpg"))
    print(Classify_Image(None,"./TestingData/Test_Image4.jpg"))
    print(Classify_Image(None,"./TestingData/Test_Image5.jpg"))
#Contributor Kamalpreet Singh(21103029)