from flask import Flask, request, jsonify
from flask import Response
import json

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def handle_get():
    # GET 요청의 쿼리 파라미터를 추출합니다.
    query_params = request.args  # ImmutableMultiDict 객체
    data = {key: query_params[key] for key in query_params.keys()}
    response_data = json.dumps({"message": "GET 요청 처리됨", "received_data": data}, ensure_ascii=False)
    return Response(response_data, mimetype='application/json')
    #return jsonify({"message": "GET 요청 처리됨", "received_data": data})

@app.route('/post', methods=['POST'])
def handle_post():
    # POST 요청의 본문을 form 데이터로부터 추출합니다.
    form_data = request.form  # ImmutableMultiDict 객체
    data = {key: form_data[key] for key in form_data.keys()}
    response_data = json.dumps({"message": "POST 요청 처리됨", "received_data": data}, ensure_ascii=False)
    return Response(response_data, mimetype='application/json')
    #return jsonify({"message": "POST 요청 처리됨", "received_data": data})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
