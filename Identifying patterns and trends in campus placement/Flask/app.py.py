from flask import Flask, render_template , request 
import pickle 
import joblib

app = Flask(__name__)
model = pickle.load(open(r"E:\project ml\placement.pkl", 'rb'))
#ct=joblib.load('placement')

@app.route('/') 
def hello(): 
    return render_template("index.html")


@app.route('/y_predict', methods=["POST"]
def y_predict():
    x_test = [[(0) for yo in request.form.values()]]
    prediction =model.predict(x_test)
    prediction prediction[0]
    return render_template("secondpage.html", y=prediction)


if __name__ == '__main__':
    app.run(debug=True)

