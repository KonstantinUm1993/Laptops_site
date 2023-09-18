import sqlite3
from flask import Flask, render_template

connection = sqlite3.connect(r"Laptops_site/tovary.db", check_same_thread=False)
cursor = connection.cursor()

app = Flask(__name__)

@app.route("/")
def site():
    return render_template("main_page.html")


@app.route("/tovary")
def assort():
    cursor.execute("select * from Laptops")
    result = cursor.fetchall()
    return render_template("goods_page.html", laptops=result)   


if __name__ ==  "__main__":
    app.run(debug=True, port = 8000)


