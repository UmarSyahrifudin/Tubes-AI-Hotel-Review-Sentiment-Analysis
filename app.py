import numpy as np
# from flask_ngrok import run_with_ngrok
from flask import Flask, render_template , request 
import pickle

model = pickle.load(open("./model_pkl", 'rb'))

app = Flask(__name__, template_folder='./templates')
# run_with_ngrok(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():    
      input = [str(x) for x in request.form.values()]
      prediction = model.predict(input)[0]

      return render_template('index.html', output=prediction, review=input)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
