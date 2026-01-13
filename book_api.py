from flask import Flask 
app = Flask(__name__)
@app.route("/books",methods=["GET"])
def get_books():
    books=[
    {"title":"book 1","author":"author 1","year":"year1"},
    {"title":"book 2","author":"author 2","year":"year2"},
    {"title":"book 3","author":"author 3","year":"year3"}
    ]
    return books

if __name__ == "__main__":
 app.run(debug="True")

