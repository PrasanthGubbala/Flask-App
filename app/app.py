from flask import Flask, request
from flask import jsonify
from flask import redirect,url_for
from flask import render_template
from flask import jsonify
import json
from models import Employee
from serializers import EmployeeSerializer

app = Flask(__name__)


dict = [
        {'id': 0,
         'title': 'A Fire Upon the Deep',
         'author': 'Vernor Vinge',
         'first_sentence': 'The coldsleep itself was dreamless.',
         'year_published': '1992'},
        {'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'},
        {'id': 2,
         'title': 'Dhalgren',
         'author': 'Samuel R. Delany',
         'first_sentence': 'to wound the autumnal city.',
         'published': '1975'}
]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login/',methods=['POST'])
def loginCheck():
    user = request.form['user']
    password = request.form['password']
    if user=='vns' and password=='vns':
        return render_template('main.html',result={'user':user})
    else:
        return render_template('login.html')


@app.route('/getall/',methods=['GET'])
def getall():
    response = app.response_class(
        response=json.dumps(dict),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/getone/<id>',methods=['GET'])
def getone(id):
    new_rec = []
    for rec in dict:
        if str(rec['id'])==id:
            new_rec.append(rec)
        else:
            pass
    # response = app.response_class(
    #     response=json.dumps(new_rec),
    #     status=200,
    #     mimetype='application/json'
    # )
    # return response
    return jsonify(new_rec)

@app.route('/getall/employees/',methods=['GET'])
def getallemployees():
    res = Employee.objects.all()
    ser = EmployeeSerializer(many=True)
    return ser.dump(res.data)


if __name__ == '__main__':
    app.run(port=105,debug=True)
