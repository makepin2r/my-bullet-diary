from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.0mtn7sx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca) 
db = client.dbsparta
count = 0 # inputData에서 사용할 ID용 카운트

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/inputData", methods=["POST"])
def inputData_post():
    todo_receive = request.form['todo_give']
    selc_receive = request.form['selc_give']
    
    # 아이디 생성을 위한 카운트 생성
    Todo_list = list(db.tododb.find({}, {'_id': False})) 
    count = count + 1 

    doc = {
        'id':count,             # id
        'selc': selc_receive,   # 불렛 종류
        'list': todo_receive,   # 텍스트
        'isChecked' : 0,        # 체크박스 체크 여부
        'isHighlighted' : 0     # 별표 여부
    }

    db.tododb.insert_one(doc)
    return jsonify({'msg': '저장완료!'})
    

# @app.route("/list", methods=["POST"])
# def list_post():
#     list_receive = request.form['list_give']

#     Todo_list = list(db.Todo.find({}, {'_id': False}))
#     count = len(Todo_list) + 1
#     doc = {
#         'id':count,             # id
#         'list': list_receive,   # 텍스트
#         'isChecked' : 0,        # 체크박스 체크 여부
#         'isHighlighted' : 0,          # 별표 여부
#     }
#     db.Todo.insert_one(doc)
#     return jsonify({'msg': '추가완료!'})

@app.route("/list/delete", methods=["POST"])
def del_post():
    num_receive = request.form['num_give']

    db.tododb.delete_one({'id': int(num_receive)})
    return jsonify({'msg': "삭제완료!"})

@app.route("/list/isChecked", methods=["POST"])
def checked_post():
    id_receive = request.form['id_give']
    check_receive = request.form['check_give']
    
    print("isChecked", check_receive, (check_receive ^ 1))

    db.tododb.update_one({'id': id_receive}, {'$set': {'isChecked': (check_receive ^ 1)}})
    return jsonify({'msg': "완료!"})

@app.route("/list/focused", methods=["POST"])
def highlighted_post():
    highlighted_receive = request.form['highlighted_give']
    id_receive = request.form['id_give']
    db.tododb.update_one({'id': id_receive}, {'$set': {'isHighlighted': (highlighted_receive ^ 1)}})
    return jsonify({'msg': "중요!"})

@app.route("/list", methods=["GET"])
def list_get():
    all_lists = list(db.tododb.find({}, {'_id': False}))
    return jsonify({'result': all_lists})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)