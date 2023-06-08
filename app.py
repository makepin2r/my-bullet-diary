from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.0mtn7sx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)      # 주소 넣기
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
    
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)