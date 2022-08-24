# Put your app in here.

from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def calc_add():
    a = request.args['a']
    b = request.args['b']
    answer = add(int(a), int(b))
    return str(answer)

@app.route('/sub')
def calc_sub():
    a = request.args['a']
    b = request.args['b']
    answer = sub(int(a), int(b))
    return str(answer)

@app.route('/mult')
def calc_mult():
    a = request.args['a']
    b = request.args['b']
    answer = mult(int(a), int(b))
    return str(answer)

@app.route('/div')
def calc_div():
    a = request.args['a']
    b = request.args['b']
    answer = div(int(a), int(b))
    return str(answer)

calc_ops = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<op>')
def handle_calc(op):
    a = request.args['a']
    b = request.args['b']
    answer = calc_ops[op](int(a), int(b))
    return str(answer)

