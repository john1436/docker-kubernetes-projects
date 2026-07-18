from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

@app.route("/health")
def health():
    return "Healthy", 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    cur = conn.cursor()

    cur.execute("SELECT id, title FROM tasks ORDER BY id")

    rows = cur.fetchall()

    cur.close()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1]
        })

    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():

    data = request.get_json()

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id;",
        (data["title"],)
    )

    task_id = cur.fetchone()[0]

    conn.commit()

    cur.close()

    return jsonify({
        "id": task_id,
        "title": data["title"]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
