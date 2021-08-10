from flask.json import jsonify
from db import index
from flask import Flask,request,app
from flask import Flask,request
from ni_sau import index

# @app.route('/palindrom',methods=['POST','GET'])
def palindrom(string):

    # input=request.form['string']
    if string[::-1]==string:
        result=True
    else:
        result=False
    return result


# @app.route('/reverse',methods=['POST','GET'])
def rev(string):
    # input=request.form['string']
    result=string[::-1]
    return result

# @app.route('/sort',methods=['POST','GET'])
def sorting(string):
    # input=request.form['input']
    def split(word):

        return [char for char in word]
    m=''
    split_str=split(string)
    sorted_string=sorted(split_str)
    for i in sorted_string:
        m=m+i
    result=m
    return result


    
app=Flask(__name__)


# @app.route('\', methods=['POST','GET'])
@app.route('/palindrom',methods=['POST','GET'])
def main():
    string=request.form.get('string')

    result=palindrom(string)
    return jsonify(result)



@app.route('/reverse',methods=['POST','GET'])
def dfd():
    string=request.form.get('string')

    result=rev(string)
    return jsonify(result)


@app.route('/sorting',methods=['POST','GET'])
def palin():
    string=request.form.get('string')

    result=sorting(string)
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)