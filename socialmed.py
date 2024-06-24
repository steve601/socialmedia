from flask import Flask,request,render_template
import pickle
import numpy as np

app = Flask(__name__)

def load_model():
    with open('socialmedia.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
model = data['model']
scaler = data['scaler']

@app.route('/')
def homepage():
    return render_template('socialmed.html')
@app.route('/predict',methods = ['POST'])
def predictor():
    try:
        # getting values from the user
        d1 = request.form['age']
        d2 = request.form['gender']
        d3 = request.form['platform']
        d4 = request.form['usg/day(mins)']
        d5 = request.form['post/day']
        d6 = request.form['likesRcved/day']
        d7 = request.form['commentsRcved/day']
        d8 = request.form['msgsSent/day']
        # let's convert gender and platform to numeric
        if d2 == 'Male':
            d2 = 0
        if d2 == 'Female':
            d2 = 1
        if d2 == 'Other':
            d2 = 2
            
        if d3 == 'Snapchat':
            d3 = 0
        if d3 == 'Telegram':
            d3 = 1
        if d3 == 'Whatsapp':
            d3 = 2
        if d3 == 'LinkedIn':
            d3 = 3
        if d3 == 'Facebook':
            d3 = 4
        if d3 == 'Twitter':
            d3 = 5
        if d3 == 'Instagram':
            d3 = 6
        # doing the prediction
        inp = np.array([[d1,d2,d3,d4,d5,d6,d7,d8]])
        prediction  = model.predict(inp)
        if prediction == 0:
            output = 'User is likely to be angry'
        if prediction == 1:
            output = 'User is likely to be bored'
        if prediction == 2:
            output = 'User is likely to be sad'
        if prediction == 3:
            output = 'User is likely to be anxious'
        if prediction == 4:
            output = 'User is likely to be happy'
        if prediction == 5:
            output = 'User is likely to be neutral'
            
        return render_template('socialmed.html',text = output)
    except:
        print('AN ERROR OCCURED!!!')
        
if __name__ == '__main__':
    app.run(host="0.0.0.0")
    
        




