from flask import jsonify

from app import app


@app.route('/api1')
def api1():
    return jsonify({"value": 12.4, "data": [5, 6, 7]})


@app.route('/api2')
def api2():
    return jsonify({"name": "thing", "score": 123.4343})

