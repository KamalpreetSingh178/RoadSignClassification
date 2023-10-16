from flask import Flask,request,jsonify
import Utilities

app=Flask(__name__)

@app.route("/Hello")#A simple API to return Hello for Testing Flask requirements
def Hello():
    return "Hello"

@app.route("/Classify_Image",methods=["GET","POST"])#HTTP REST API's-GET and POST method
def ClassifyImage():
    #The Image is to be passed as Base64 encoded String
    #Sending Image Data in a Request Object imported from request module
    image_data=request.form["image_data"]
    #This Image will be Base64 Encoded String
    #Jsonifying the Prediction to be interpreted by Javascript on the Frontend
    response=jsonify(Utilities.Classify_Image(image_data))
    #To be Handled during Frontend Development

    #Adding Access,Control,Allow and Origin
    response.headers.add("Access-Control-Allow-origin","*")
    return response

if __name__=="__main__":
    app.run(port=5000)
#Contributor Kamalpreet Singh(21103029)