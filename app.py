from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

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
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)