from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

#importing the models
scaler = pickle.load(open('models/scaler.pkl', 'rb'))
model = pickle.load(open('models/model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method=='POST':
        Pregnant=int(request.form.get("Pregnant"))
        Glucose=float(request.form.get("Glucose"))
        Diastolic_BP=float(request.form.get("Diastolic_BP"))
        BMI=float(request.form.get("BMI"))
        Diabetes_Pedigree=float(request.form.get("Diabetes_Pedigree"))
        Age=float(request.form.get("Age"))
        data=scaler.transform([[Pregnant, Glucose, Diastolic_BP, BMI, Diabetes_Pedigree, Age]])
        output=model.predict(data)
        return render_template('index.html', prediction_text="The person is diabetic" if output[0]==1 else "The person is not diabetic")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")