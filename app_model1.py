from flask import Flask,request,render_template
import numpy as np
import pandas
import sklearn
import pickle

# Importar los modelos
model = pickle.load(open('model.pkl','rb'))
sc = pickle.load(open('standscaler.pkl','rb'))
enc = pickle.load(open('encoder.pkl','rb'))

# crear flask
app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    G = request.form['Gender']
    E = int(request.form['Age'])
    I = float(request.form['Income'])
    S = int(request.form['Score'])

    feature_list = [G, E, I, S]
    single_pred = np.array(feature_list).reshape(1, -1)

    transformed_features = enc.transform(single_pred)
    transformed_features[:,2:] = sc.transform(transformed_features[:,2:])
    prediction = model.predict(transformed_features)

    diccionario = {1: "Grupo 1", 2: "Grupo 2", 3: "Grupo 3", 4: "Grupo 4", 5: "Grupo 5"}

    if prediction[0] in diccionario:
        crop = diccionario[prediction[0]]
        result =("El cliente pertenece al : {} ".format(crop))
    else:
        result =("Sorry, El cliente no pertenece a ningun grupo")
    return render_template('index.html',result = result)

# python main
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
