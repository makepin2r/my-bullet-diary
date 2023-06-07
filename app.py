from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.ofgcrbp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/list", methods=["POST"])
def list_post():
    list_receive = request.form['list_give']

    Todo_list = list(db.Todo.find({}, {'_id': False}))
    count = len(Todo_list) + 1
    doc = {
        'num':count,  
        'list': list_receive,
        'done' : 0   
    }
    db.Todo.insert_one(doc)
    return jsonify({'msg': '추가완료!'})

@app.route("/list/delete", methods=["POST"])
def del_post():
    num_receive = request.form['num_give']
    db.Todo.delete_one({'num': int(num_receive)})
    return jsonify({'msg': "삭제완료!"})

    
@app.route("/list", methods=["GET"])
def list_get():
    
    all_lists = list(db.Todo.find({}, {'_id': False}))
    return jsonify({'result': all_lists})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)