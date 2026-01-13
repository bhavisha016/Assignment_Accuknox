from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="assignment_db"
)

cursor = db.cursor()

@app.route("/students")
def students():
    cursor.execute("SELECT name, total_score FROM students_scores")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "name": row[0],
            "score": row[1]
        })

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
