from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.0mtn7sx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca) 
db = client.dbsparta
count = 0

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/login", methods=["POST"])
def login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give'] # 암호화 필요
    print(id_receive)
    print(pw_receive)
    # 유효성 체크 후 결과값 전송
    msg = False
    if True:
        msg = True
    else:
        msg = False
    return jsonify({'result': msg})

@app.route("/inputData", methods=["POST"])
def inputData_post():
    global count
    todo_receive = request.form['todo_give']
    selc_receive = int(request.form['selc_give'])

    
    # 아이디 생성을 위한 카운트 생성
    count = count + 1 

    doc = {
        'id':count,             # id
        'selc': selc_receive,   # 불렛 종류
        'list': todo_receive,   # 텍스트
        'isChecked' : 0,        # 체크박스 체크 여부
        'isHighlighted' : 0     # 별표 여부
    }

    test = db.tododb.insert_one(doc)
    print(test)
    return jsonify({"msg": "저장완료!"})
    

@app.route("/list/delete", methods=["POST"])
def del_post():
    num_receive = request.form['num_give']

    db.tododb.delete_one({'id': int(num_receive)})
    return jsonify({'msg': "삭제완료!"})

@app.route("/list/isChecked", methods=["POST"])
def checked_post():
    id_receive = int(request.form['id_give'])
    check_receive = int(request.form['check_give'])
    
    db.tododb.update_one({'id': id_receive}, {'$set': {'isChecked': (check_receive ^ 1)}})
    return jsonify({'msg': "완료!"})

@app.route("/list/focused", methods=["POST"])
def focused_post():
    focused_receive = request.form['focused_give']

    db.tododb.update_one({'focused': int(focused_receive)}, {'$set': {'focused': 1}})
    return jsonify({'msg': "중요!"})

@app.route("/list", methods=["GET"])
def list_get():
    all_lists = list(db.tododb.find({}, {'_id': False}))
    return jsonify({'result': all_lists})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)