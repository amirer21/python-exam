import requests
import json

def send_get_request(url, params):
    # 헤더에 'Content-Type'을 'application/json'으로 설정
    #headers = {'Content-Type': 'application/json'}    
    headers = {'Content-Type': 'application/json; charset=utf-8'}   
    try:
        # GET 요청 보내기
        response = requests.get(url, params=params, headers=headers)
        response_data = response.json()
        #print(f"GET 요청에 대한 응답: {response.text}")
        print(f"GET 요청에 대한 응답: {response_data}")
    except requests.exceptions.RequestException as e:
        print(f"GET 요청 오류: {e}")
        
def send_post_request(url, data):
    # JSON으로 인코딩할 데이터
    json_data = json.dumps(data)    
    # 헤더에 'Content-Type'을 'application/json'으로 설정
    #headers = {'Content-Type': 'application/json'}    
    headers = {'Content-Type': 'application/json; charset=utf-8'}    
    try:
        # POST 요청 보내기
        response = requests.post(url, data=json_data, headers=headers)
        response_data = response.json()
        #print(f"POST 요청에 대한 응답: {response.text}")
        print(f"POST 요청에 대한 응답: {response_data}")
    except requests.exceptions.RequestException as e:
        print(f"POST 요청 오류: {e}")

# 실행 예시
if __name__ == "__main__":
    # 실행 전에 서버 주소를 적절히 설정하세요.
    test_get_url = "http://localhost:5000/get"
    test_post_url = "http://localhost:5000/post"
    # GET 요청에 사용될 쿼리 파라미터
    get_params = {'key1': 'value1', 'key2': 'value2'}    
    # POST 요청에 사용될 JSON 데이터
    post_data = {'key1': 'value1', 'key2': 'value2'}
    
    send_get_request(test_get_url, get_params)
    send_post_request(test_post_url, post_data)



"""
Flask에서는 jsonify를 사용하여 JSON 응답을 생성할 때, 기본적으로 utf-8 인코딩을 사용합니다.
따라서 jsonify 함수가 반환하는 응답은 일반적으로 한글 문자를 포함할 수 있으며, 
이 문자들은 정상적으로 인코딩되어 클라이언트에 전송됩니다.

응답에서 한글이 유니코드 이스케이프 시퀀스로 나타나는 문제는 주로 클라이언트 측에서 응답 본문을 해석하는 방식에 관련된 문제일 수 있습니다.
하지만, Flask 서버 측에서 응답의 Content-Type 헤더에 charset=utf-8을 명시적으로 추가함으로써 클라이언트에게 정확한 인코딩 타입을 알려줄 수 있습니다. 이는 클라이언트가 응답을 올바르게 인코딩하여 해석할 수 있도록 도와줍니다.
"""