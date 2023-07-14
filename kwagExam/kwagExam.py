#  **kwargs (키워드 인수)

import json
from dataclasses import dataclass

# 어떤 JSON 데이터를 기존에 구성해둔 DTO 클래스에 매핑하는 방법
# 파이썬에서는 ** 키워드가 있다. 이 키워드는 딕셔너리를 풀어서 함수의 인자로 전달해준다.
# **kwargs(키워드 인수): dictionary - Key가 별도의 keyword 인수가 되고 Value이 이러한 인수의 값이 됩니다 .

#DTO 클래스를 정의한다.
@dataclass
class KwagExamClass:
    key1: str
    key2: int
    key3: bool
    key4: ['test', 'test2']

#JSON 데이터를 정의한다.
json_str = '''
{
    "key1": "value1",
    "key2": 123,
    "key3": true,
    "key4": ["test", "test2"]
}
'''

#JSON 문자열을 JSON 객체로 변환한다.
json_obj = json.loads(json_str)

# ** 키워드를 사용하여 JSON 객체를 KwagExamClass 클래스의 객체에 매핑한다.
my_object = KwagExamClass(**json_obj)

# 값이 잘 맵핑되었는지 확인해보기
print(my_object.key1)  # Output: value1
print(my_object.key2)  # Output: 123
print(my_object.key3)  # Output: True
print(my_object.key4)  # Output: ['test', 'test2']

# *arg, **kwargs : https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs