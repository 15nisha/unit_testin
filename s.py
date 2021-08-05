from flask import Flask,request,app
from flask import Flask,request

# @app.route('/palindrom',methods=['POST','GET'])
def palindro(string):

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
@app.route('/',methods=['POST','GET'])
def main():
    # string=request.form.get('string')
    try:


        string=request.form.get('string')
    # y=request.form.get('y')

        result=palindro(string)
        result=rev(string)
        result=sorting(string)
        return (result)

    except:

        return 'please enter value'

    # return (result)


if __name__ == '__main__':
    app.run(debug=True)