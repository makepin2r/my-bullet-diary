from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.0mtn7sx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca) 
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/inputData", methods=["POST"])
def inputData_post():
    todo_receive = request.form['todo_give']
    selc_receive = request.form['todo_give']
    
    doc = {"database":[
            {
                'todo': todo_receive,
                'selc': selc_receive

            }
        ]
    }
    db.tododb.insert_one(doc)
    return jsonify({'msg': '저장완료!'})
    

@app.route("/list", methods=["POST"])
def list_post():
    list_receive = request.form['list_give']

    Todo_list = list(db.Todo.find({}, {'_id': False}))
    count = len(Todo_list) + 1
    doc = {
        'num':count,  
        'list': list_receive,
        'isChecked' : 0,
        'focused' : 0,   
    }
    db.Todo.insert_one(doc)
    return jsonify({'msg': '추가완료!'})

@app.route("/list/delete", methods=["POST"])
def del_post():
    num_receive = request.form['num_give']

    db.Todo.delete_one({'num': int(num_receive)})
    return jsonify({'msg': "삭제완료!"})

@app.route("/list/isChecked", methods=["POST"])
def checked_post():
    check_receive = request.form['check_give']

    db.Todo.update_one({'isChecked': int(check_receive)}, {'$set': {'isChecked': 1}})
    return jsonify({'msg': "완료!"})

@app.route("/list/focused", methods=["POST"])
def focused_post():
    focused_receive = request.form['focused_give']

    db.Todo.update_one({'focused': int(focused_receive)}, {'$set': {'focused': 1}})
    return jsonify({'msg': "중요!"})

@app.route("/list", methods=["GET"])
def list_get():
    all_lists = list(db.Todo.find({}, {'_id': False}))
    return jsonify({'result': all_lists})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)