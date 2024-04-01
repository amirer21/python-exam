import requests

def send_get_request(url, params):
    """
    주어진 URL에 대해 GET 요청을 보내고 응답을 출력합니다.
    :param url: 요청을 보낼 URL
    :param params: GET 요청과 함께 보낼 쿼리 파라미터 (사전 형태)
    
    params 인자
    
    목적: params 인자는 URL의 쿼리 스트링에 데이터를 추가하기 위해 사용됩니다. 이는 주로 GET 요청에서 사용되며, 서버에 데이터를 전달하는 방법입니다.
    사용 예: requests.get("http://example.com/api", params={"key": "value"})는 요청을 보낼 때 URL을 http://example.com/api?key=value로 만듭니다. 이 방식은 서버에 정보를 요청할 때, 필터, 정렬 방식 등의 옵션을 전달하는 데 사용됩니다.
    작동 방식: 지정된 사전형 객체(params)의 키와 값을 URL의 쿼리 스트링으로 변환하여 요청 URL에 추가합니다. 이때 키와 값은 URL 인코딩되어 안전하게 전송됩니다.
    """
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.get(url, params=params, headers=headers)
        print(f"GET 요청에 대한 응답: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"GET 요청 오류: {e}")
        
def send_post_request(url, data):
    """
    주어진 URL에 대해 POST 요청을 보내고 응답을 출력합니다.
    :param url: 요청을 보낼 URL
    :param data: POST 요청과 함께 보낼 데이터 (사전 형태)
    
    data 인자
    
    목적: data 인자는 HTTP 요청의 본문(body)에 데이터를 포함시키기 위해 사용됩니다. 이는 주로 POST, PUT, PATCH 요청에서 사용되며, 서버에 데이터를 생성하거나 업데이트하기 위한 목적으로 사용됩니다.
    사용 예: requests.post("http://example.com/api", data={"key": "value"})는 HTTP 요청의 본문에 key=value 형태의 데이터를 포함시켜 전송합니다. 이 방식은 서버에 새로운 자원을 생성하거나 기존 자원을 업데이트할 때 주로 사용됩니다.
    작동 방식: 지정된 사전형 객체(data)를 application/x-www-form-urlencoded 형식의 문자열로 변환하여 HTTP 요청의 본문에 포함시킵니다. 클라이언트와 서버 간에 복잡한 데이터 구조를 전송할 필요가 있을 때 사용됩니다.
    """
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(url, data=data, headers=headers)
        print(f"POST 요청에 대한 응답: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"POST 요청 오류: {e}")


# 실행 예시 (실제 실행 시 사용할 서버의 URL로 변경해야 합니다.)
if __name__ == "__main__":
    # 실행 전에 서버 주소를 적절히 설정하세요.
    test_url = "http://localhost:5000"
    
    # GET 요청 실행 예
    get_params = {'key1': 'value1', 'key2': 'value2'}
    send_get_request(f"{test_url}/get", get_params)
    
    # POST 요청 실행 예
    post_data = {'key1': 'value1', 'key2': 'value2'}
    send_post_request(f"{test_url}/post", post_data)
