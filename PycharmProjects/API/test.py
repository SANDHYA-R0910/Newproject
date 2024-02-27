from flask import Flask, request, jsonify


app = Flask(__name__)
# GET---> via url ex: data science
# POST---> via body ex: gmail email id & password
@app.route('/abc',methods=['GET','POST'])
def test1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))

@app.route('/abc1/sudh',methods=['GET','POST'])
def test2():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))

@app.route('/abc1/sudh/test',methods=['GET','POST'])
def test4():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a ** b
        return jsonify((str(result)))

@app.route('/abc1/sudh/test3',methods=['GET','POST'])
def test3():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify((result))

if __name__ == '__main__':
    app.run()


# 1. write a program to insert a record in sql table via api
# 2.update a record via api
# 3. delete a record via api
# 4. fetch a record vias api

def f1(a,b):
    return a+b



