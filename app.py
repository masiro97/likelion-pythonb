from flask import Flask, render_template, request
import requests
import bs4

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"
    
@app.route("/<name>")
def john(name):
    return "hello {}".format(name)
    
# 엄청 간단한 계산기
# return String
@app.route("/cube/<num>")
def cube(num):
    num = int(num)
    cube = num ** 3
    return "cube : {}".format(cube)
    
@app.route("/show")
def show():    
    return render_template('index.html')
    
@app.route("/lol")
def lol():
    return render_template("lol.html")

@app.route("/stat")
def stat():
    id = request.args.get('id')
    # id에 담긴 정보를 가지고
    # op.gg에 요청을 보내 전적을 가지고 와서
    # 그 중에서 win & lose 정보만 받아온다.
    url = "http://www.op.gg/summoner/userName="
    response = requests.get(url + id)
    html = bs4.BeautifulSoup(response.text)
    win = html.select_one("#GameAverageStatsBox-summary > div.Box > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > span.win")
    lose = html.select_one("#GameAverageStatsBox-summary > div.Box > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > span.lose")
    return render_template("stat.html",id = id, win=win.text, lose =lose.text)