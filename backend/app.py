from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

# Wait until DB is ready
while True:
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="demo"
        )
        break
    except:
        time.sleep(2)

@app.route("/")
def home():
    cursor = db.cursor()
    cursor.execute("SELECT 'Hello from MySQL via Backend API!'")
    result = cursor.fetchone()
    return f"RESPONSE: {result[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
