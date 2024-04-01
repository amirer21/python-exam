from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def handle_get():
    try:
        query_params = request.args
        data = {key: query_params[key] for key in query_params.keys()}
        response = jsonify({"message": "GET 요청 처리됨", "received_query_params": data})
        response.headers['Content-Type'] = "application/json; charset=utf-8"
        return response
    except Exception as e:
        return jsonify({"message": "GET 요청 처리 중 오류 발생", "error": str(e)}), 500

@app.route('/post', methods=['POST'])
def handle_post():
    try:
        json_data = request.get_json()
        if json_data is None:
            return jsonify({"message": "POST 요청 처리됨", "error": "Invalid or missing JSON data"}), 400
        response = jsonify({"message": "POST 요청 처리됨", "received_json_data": json_data})
        response.headers['Content-Type'] = "application/json; charset=utf-8"
        return response
    except Exception as e:
        return jsonify({"message": "POST 요청 처리 중 오류 발생", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
