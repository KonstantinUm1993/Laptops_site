import sqlite3
from flask import Flask, render_template, request


connection = sqlite3.connect(r"Laptops_site/tovary.db", check_same_thread=False)
cursor = connection.cursor()

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def site():
    page = 1
    if request.method=="POST":
        search=request.form["Search"]
        print(search)
        cursor.execute(f"select * from Laptops WHERE Vendor LIKE '%{search}%'")
        result = cursor.fetchall()
        print(result)
        numb_of_goods=len(result)
        return render_template("goods_page.html", laptops=result, page=page, numb_of_goods=numb_of_goods)   
    else:
        return render_template("main_page.html")

@app.route("/tovary", methods=["POST","GET"])
def assort_0():
    page = 1
    if request.method=="POST":
        search=request.form["Search"]
        print(search)
        cursor.execute(f"select * from Laptops WHERE Vendor LIKE '%{search}%'")
        result = cursor.fetchall()
        print(result)
        numb_of_goods=len(result)
        return render_template("goods_page.html", laptops=result, page=page, numb_of_goods=numb_of_goods) 
    else:
        cursor.execute("select * from Laptops WHERE id < 10")
        result = cursor.fetchall()
        cursor.execute("select count(ID) from Laptops")
        len_of_id = cursor.fetchall()
        numb_of_goods = len_of_id[0][0]
        return render_template("goods_page.html", laptops=result, page=page, numb_of_goods=numb_of_goods)  


@app.route("/tovary&p1", methods=["POST","GET"])
def assort_1():
    page = 1
    if request.method=="POST":
        search=request.form["Search"]
        print(search)
        cursor.execute(f"select * from Laptops WHERE Vendor LIKE '%{search}%'")
        result = cursor.fetchall()
        print(result)
        numb_of_goods=len(result)
        return render_template("goods_page.html", laptops=result, page=page, numb_of_goods=numb_of_goods) 
    else:
        cursor.execute("select * from Laptops WHERE id < 10")
        result = cursor.fetchall()
        cursor.execute("select count(ID) from Laptops")
        len_of_id = cursor.fetchall()
        numb_of_goods = len_of_id[0][0]
        return render_template("goods_page.html", laptops=result, page=page, numb_of_goods=numb_of_goods) 

@app.route("/tovary&p2", methods=["POST","GET"])  
def assort_2():
    page = 2
    if request.method=="POST":
        search=request.form["Search"]
        print(search)
        cursor.execute(f"select * from Laptops WHERE Vendor LIKE '%{search}%'")
        result = cursor.fetchall()
        print(result)
        numb_of_goods=len(result)
        return render_template("goods_page.html", laptops=result, page=page, numb_of_goods=numb_of_goods)
    else: 
        cursor.execute("select * from Laptops WHERE id > 9")
        result = cursor.fetchall()
        cursor.execute("select count(ID) from Laptops")
        len_of_id = cursor.fetchall()
        numb_of_goods = len_of_id[0][0]
        return render_template("goods_page.html", laptops=result, page=page, numb_of_goods=numb_of_goods)   

if __name__ ==  "__main__":
    app.run(debug=True, port = 8000)


