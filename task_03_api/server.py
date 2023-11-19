from flask import Flask, request, jsonify
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from my_lib.conn_post import ConnPost

app = Flask(__name__)


@app.route("/get_day", methods=["POST"])
def get_day():
    day = request.json.get("day")
    conn = ConnPost()
    query = (
        f"""
        SELECT
            *
        FROM news 
        where date(load_dttm) = '{day}'
        """
    )
    data = conn.get_query(query)
    return jsonify({"answer": data})


@app.route("/get_like", methods=["POST"])
def get_like():
    word = request.json.get("word")
    conn = ConnPost()
    query = (
        f"""
            SELECT
                *
            FROM news
            WHERE content LIKE '%{word}%';
        """
    )
    data = conn.get_query(query)
    return jsonify({"answer": data})


if __name__ == "__main__":
    app.run("localhost", 5000)
