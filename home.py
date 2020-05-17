import numpy as np
import pandas as pd
import pickle
from flask import Flask
from flask import render_template
import os
from flask import request,jsonify


app=Flask(__name__, template_folder='templates')
#model = pickle.load(open(f"C:\Python\Scripts\MyWorkspace\Logistic Regression\\finalized_model.sav", 'rb'))
model = pickle.load(open(f"finalized_model.pkl", 'rb'))
app.root_path = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def helloworld():
    return '''<html>
    <head>
        <title>Hello Flask</title>
     </head>

            <body>
            <form action = "Predict", method ="POST">
                 <table>
                 <tbody>
             <tr> <td>Age</td><td><input type="text" id="txtAge" name="Age"></td>  </tr>
               <tr><td>Experiencce</td><td><input type="text" name="Experiencce"></td> </tr>
                        <tr><td>Income</td><td><input type="text" name="Income"></td> </tr>               
                <tr><td>Family</td><td><input type="text" name="Family"></td> </tr>                
                <tr><td>CCAvg</td><td><input type="text" name="CCAvg"></td> </tr>
                <tr><td>EDucation</td><td><input type="text" name="EDucation"></td> </tr>
                <tr><td>Mortgage</td><td><input type="text" name="Mortgage"></td> </tr>              
                <tr><td>CDAccount</td><td><input type="text" name="CD Account"></td> </tr>
                 <!-- <tr><td>Online_Yes</td><td><input type="text" name="Online_Yes"></td> </tr> 
                <tr><td>Securities Account_Yes'</td><td><input type="text" name="SecuritiesAccount_Yes"></td> </tr>
                
                <tr><td>EDu_level_3</td><td><input type="text" name="EDu_level_3"></td> </tr>
                <tr><td>Creditcard_Yes</td><td><input type="text" name="Creditcard_Yes"></td> </tr>
                -->
               <tr><td></td><td> <input type="submit" value="Predict"></tr></td>
                </tbody>
          </table>
          </form>
            </body>
</html>'''
    # return render_template('index.html')




@app.route('/Predict', methods=['POST'])
def predict():
    try:
        int_features = [int(x) for x in request.form.values() if x is not None ]
        final_features = [np.array(int_features)]
        predictions = model.predict(final_features)
        output =predictions[0]
        return  f"Model Prediction is {output}"  #'''<html>
    # <head>
    #     <!-- <title>Hello Flask</title> -->
    #  </head>

    #         <body>
    #       <table>
    #           <p>Model Prediction is {{output}}</p>
    #         </body>
    #         </html>'''
    except:
        print("Error Occured")    


@app.route('/demo', methods=['POST'])
def demo():
    data = {}
    age = request.form['Age']
    Income = request.form['Income']   
    ZIPCode = request.form['ZIPCode']
    Family = request.form['Family']
    CCAvg = request.form['CCAvg']
    Mortgage = request.form['Mortgage']
    Online_Yes = request.form['Online_Yes']
    CDAccount_Yes  =  request.form['CDAccount_Yes']
    SecuritiesAccount_Yes = request.form['SecuritiesAccount_Yes']
    EDu_level_2 =request.form['EDu_level_2']
    EDu_level_3=request.form['EDu_level_3']
    Creditcard_Yes =request.form['Creditcard_Yes']
     
    data["Age"] = age
    data["Income"] = Income
    data["ZIPCode"] = ZIPCode
    data["Family"] = Family
    data["CCAvg"] = CCAvg
    data["Mortgage"] = Mortgage
    data["Online_Yes"] = Online_Yes
    data["CDAccount_Yes"] = CDAccount_Yes
    data["SecuritiesAccount_Yes"] = SecuritiesAccount_Yes
    data["EDu_level_2"] = EDu_level_2
    data["EDu_level_3"] = EDu_level_3
    data["Creditcard_Yes"] = Creditcard_Yes
    #features = [age,Income, ZIPCode, Family, CCAvg, Mortgage, Online_Yes, CDAccount_Yes,SecuritiesAccount_Yes,EDu_level_2,EDu_level_3,Creditcard_Yes]// data.values()


    #int_features = [int(x) for x in request.form.values()]
    int_features = [int(x) for x in request.form.values() if x is not None ]
    final_features = [np.array(int_features)]
    predictions = model.predict(final_features)

    #predict = model.predict(features)
    output =predictions[0]
    #output = str(predict)
    print(predict)
    data["output"] = output

    return    request.form.values() #data #request.form['Age']



if __name__ == '__main__':
    app.debug = True
    app.run()

