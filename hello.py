from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요 OOO입니다."
    
@app.route("/hello")    
def hello():
    return "짐이 묻건데 네 이름을 말하거라."
    
@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하심까? 신입사원 OOO입니다</h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1>여러 줄 보내기</h1>
    <ul>
        <li>쭉쭉쭉쭉 쭉쭉쭉쭉</li>
        <li>언제까지 어깨춤을</li>
        <li>추게할거야~</li>
        <li>내어깨를 봐</li>
        <li>탈골됐잖아</li>
    </ul>
    """
    
@app.route("/html_render")
def html_render():
    return render_template("index.html")


@app.route("/html_name/<string:name>/<float:age>/<int:money>/<path:time>")    
def html_name(name, age, money, time):
    return render_template("hello.html", your_name = name, your_age = age, your_money = money, your_time = time)
    
    
@app.route("/math/<int:num>")
def math(num):
    result = num**3
    result2 = num**5
    return render_template("math.html", my_num = num, result = result, result2 = result2)

@app.route("/dinner")
def dinner():
    list = ["편의점 도시락", "삼겹살", "간짜장", "집밥"]
    dict = {
        "편의점 도시락" : "http://news.tongplus.com/site/data/img_dir/2018/05/11/2018051101935_0.jpg",
        "삼겹살" : "http://cdn.jinfooduae.com/wp-content/uploads/2017/04/%EC%98%A4%EC%82%BC%EA%B2%B9%EC%82%B42-400x400.jpg",
        "간짜장" : "http://upload2.inven.co.kr/upload/2017/06/13/bbs/i15369150919.jpg",
        "집밥" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp3ACKaqsZK3w2cvOcpt_L6B2udYMf2BcdqcrFaRs80idFgf4p"
    }
    pick = random.choice(list)
    url = dict[pick]
    return render_template("dinner.html", pick = pick, url = url)
    
    
    
    