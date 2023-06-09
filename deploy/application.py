from flask import Flask, url_for, render_template, request, jsonify, session, redirect
application = app = Flask(__name__, static_url_path='/static')
app.secret_key = "ah#jsdl2!sdl@jslkd!hg4as9lk"

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.0mtn7sx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca) 
db = client.dbsparta
count = 0

ID = "test"
PW = "zbxlQhWkr7wh"

@app.route('/')
def home():
    if "userID" in session:
        print("userID", session["userID"])
        return render_template("index.html", username = session.get("userID"), login = True)
    else:
        print("no userID")
        return render_template("login.html", login = False)
    


@app.route("/login", methods=["GET","POST"])
def login():
    global ID, PW
    id_receive = request.args.get("loginID")
    pw_receive = request.args.get("loginPW")

    if ID == id_receive and PW == pw_receive:
        print(id_receive, pw_receive)
        session["userID"] = id_receive
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))

@app.route("/inputData", methods=["POST"])
def inputData_post():
    todo_receive = request.form['todo_give']
    selc_receive = int(request.form['selc_give'])

    # 아이디 생성을 위한 카운트 생성
    Todo_list = list(db.tododb.find({}, {'_id': False})) 
    doc = {
        'id':len(Todo_list),             # id
        'selc': selc_receive,   # 불렛 종류
        'list': todo_receive,   # 텍스트
        'isChecked' : 0,        # 체크박스 체크 여부
        'isHighlighted' : 0     # 별표 여부
    }

    db.tododb.insert_one(doc)
    return jsonify({'msg': '저장완료!'})

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
def highlighted_post():
    highlighted_receive = request.form['highlighted_give']
    id_receive = request.form['id_give']
    print('test : '+id_receive)
    print(int(highlighted_receive))
    db.tododb.update_one({'id' : int(id_receive)}, {'$set': {'isHighlighted': int(highlighted_receive)}})
    return jsonify({'msg': "중요!"})

@app.route("/list", methods=["GET"])
def list_get():
    all_lists = list(db.tododb.find({}, {'_id': False}))
    return jsonify({'result': all_lists})

if __name__ == '__main__':
    app.run()