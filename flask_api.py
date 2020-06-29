# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template,url_for,request
from gevent.pywsgi import WSGIServer
import pandas as pd 
import pickle
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        impactedapplication = request.form['u_impacted_application']
        cmdbci=request.form['cmdb_ci']
        portfolio=request.form['u_portfolio']
        environment=request.form['u_environment']
        #vect = enc.transform([[impactedapplication,cmdbci,portfolio,environment]]).toarray()
        my_prediction = clf.predict([[impactedapplication,cmdbci,portfolio,environment]])
    return render_template('result.html',prediction = my_prediction)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    