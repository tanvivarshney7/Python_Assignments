from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prasanvi@21",
        database="school_db"
    )


#1. Show a welcome message on the home route
#Create a route for the URL / that returns a plain JSON response with a welcome message. This confirms your
# Flask app is running correctly.
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the School API"})


#2. Return all students from the database
#Create a route that connects to the database, fetches every row from the students table, and returns them all
# as a JSON list.
@app.route("/students")
def students():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)


#3. Return a single student by their ID
#Create a route that accepts a student ID in the URL and returns only that student's data. If the ID does not exist,
# return a JSON message saying Student not found.
@app.route("/students/<id>")
def student(id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        return jsonify(result)
    return jsonify({"message": "Student not found"}), 404


#4. Filter students by city
#Create a route that accepts a city name in the URL and returns all students from that city. The search should be
# case-insensitive (Toronto and toronto return the same result).
@app.route("/students/city/<city>")
def city(city):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE city=%s", (city,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)


#5. Filter students by grade
#Create a route that accepts a grade (A, B, or C) in the URL and returns all students who have that grade. Return
# a message if no students match.
@app.route("/students/grade/<grade>")
def grade(grade):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE grade=%s", (grade,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    if result:
        return jsonify(result)
    return jsonify({"message": "No students found"}), 404


#6. Return a count summary of students per city
#Create a route that returns how many students are in each city. Use SQL GROUP BY and COUNT to get the results — do
# not count manually in Python.
@app.route("/students/summary/city")
def summary_city():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT city, COUNT(*) AS Total FROM students GROUP BY city")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)


#7. Return a count summary of students per grade
#Create a route that returns how many students are in each grade (A, B, C). Similar to the city summary but grouped
# by grade instead.
@app.route("/students/summary/grade")
def summary_grade():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT grade, COUNT(*) AS Total FROM students GROUP BY grade")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)


#8. Search students by name
#Create a route that accepts a search term as a URL query parameter and returns all students whose name contains that
#term. The search should be case-insensitive.
@app.route("/students/search")
def search():
    name = request.args.get("name", "")
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE name LIKE %s", (f"%{name}%",))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)




