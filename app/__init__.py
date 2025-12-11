from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction/', methods=['POST'])
def prediction():
    date = request.form['date']
    year = request.form['date'][:4]
    month = request.form['date'][5:7]
    day = request.form['date'][8:10]
    
    data = [year, month, day]
    model = joblib.load('app/model/cop_predictor.pkl')
    prediction = model.predict([data])
    
    return render_template('index.html', prediction=round(prediction[0], 2), date=date)