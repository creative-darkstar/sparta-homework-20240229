# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
from flask import Flask, render_template, request
from rsp_game_web import *

app = Flask(__name__)

import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "database.db")

db = SQLAlchemy(app)


class RSPGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    computer = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(100), nullable=False)

# [DB 생성 코드]
# with app.app_context():
#     db.create_all()


@app.route("/")
def game():
    # 데이터 정의 및 초기화
    user_input = None
    result = None
    
    # 가위 바위 보 게임 진행
    user_input = request.args.get('query')
    if user_input:
        result = play_game_web(user_input.lower())
        if result:
            row = RSPGame(computer=result["Computer"], user=result["User"], result=result["Result"])
            db.session.add(row)
            db.session.commit()
    
    # 이전 기록 DB에서 가져오기
    results = RSPGame.query.all()
    
    # Html로 전송할 데이터 담기
    data = {
        "Current": result,
        "Statistic": [
            RSPGame.query.filter_by(result="승리").count(),
            RSPGame.query.filter_by(result="패배").count(),
            RSPGame.query.filter_by(result="무승부").count()],
        "Results": results}
    
    # 데이터 전송
    return render_template('rsp_game.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
