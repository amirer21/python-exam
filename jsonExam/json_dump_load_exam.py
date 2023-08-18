import json

# Creating a dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("data type :: ", type(data))


dumped_data = json.dumps(data)
print("dumped_data :: ", dumped_data)
print("dumped_data data type :: ", type(dumped_data))

# Writing the dictionary to a JSON file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading the JSON file and loading the data back into a dictionary
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print(loaded_data)
#{'name': 'John', 'age': 30, 'city': 'New York'}
print("loaded_data type :: ", type(loaded_data))
# loaded_data type ::  <class 'dict'>


'''
data.라는 사전을 만듭니다 
"data.json"이라는 JSON 파일에 사전을 json.dump()쓰는 데 사용합니다 .data
json.load()그런 다음 "data.json" 파일에서 데이터를 읽고 사전에 다시 로드하는 데 사용합니다 loaded_data.
loaded_data마지막으로, 원래 사전과 동일한 사전을 인쇄합니다 data.'''

'''
json.dumps() : 자료형을 JSON 형태로 (단순 문자열입니다!) 바꿔준다.
json.loads() : 문자열 자료를 파싱하여 Dictionary 의 Key, Value 형태로 변경해준다.
파이썬에서는 JSON 타입의 데이터를 Dictionary로 주로 처리하고 외부로 전달할 때는 JSON 형태로 바꾸어 전달한다.
'''


# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

# Accessing values in the dictionary
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
print("GPA:", student["gpa"])

# Modifying values in the dictionary
student["age"] = 23
student["gpa"] = 3.9

# Adding a new key-value pair
student["university"] = "XYZ University"

# Deleting a key-value pair
del student["major"]

# Iterating through dictionary keys and values
for key, value in student.items():
    print(key, ":", value)

# Checking if a key exists in the dictionary
if "age" in student:
    print("Age:", student["age"])
else:
    print("Age not found")

# Getting a default value if key is not found
print("Major:", student.get("major", "N/A"))

# Getting all keys and values as lists
keys = list(student.keys())
values = list(student.values())

# Getting the number of key-value pairs in the dictionary
num_entries = len(student)

# Clearing all entries from the dictionary
#student.clear()

# Printing the modified dictionary
print(student)
#{'name': 'Alice', 'age': 23, 'gpa': 3.9, 'university': 'XYZ University'}



###########
'''
사진(Dictionary) 형태로 데이터의 구조화된 표현을 만드는 예제 코드
to_dict() 메서드는 객체의 속성을 사전(Dictionary) 형태로 변환하기 위한 커스텀 메서드입니다.
일반적으로 개체의 상태를 키-값 쌍의 컬렉션으로 나타내려는 경우에 사용됩니다.

'''
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city
        }


# Creating an instance of the Person class
person = Person("John", 30, "New York")

# Converting the instance to a dictionary using to_dict()
person_dict = person.to_dict()

# Printing the dictionary
print(person_dict)
#{'name': 'John', 'age': 30, 'city': 'New York'}



#json
'''
JSON(JavaScript Object Notation)은 서버와 웹 애플리케이션 간의 데이터 교환에 일반적으로 사용되는 경량(lightweight) 데이터 교환 형식이다.
이 방법은 네트워크를 통해 쉽게 전송하거나 파일에 저장할 수 있는 형식으로 데이터를 직렬화하려는 경우에 유용하다.

dumps 메서드는 jsonPython 객체(일반적으로 사전)를 JSON 형식 문자열로 변환하는 데 사용되는 Python 의 라이브러리에서 제공하는 메서드이다.
'''
#double quotes
json_data = {
    "name": "John",
    "age": 30
}


#single quotes
single_quotes_json_data = {
    'name': 'John',
    'age': 30
}

print("json_data :: ", json_data)
print("json_data type :: ", type(json_data))

print("single_quotes_json_data :: ", single_quotes_json_data)
print("single_quotes_json_data type :: ", type(single_quotes_json_data))

#json dump
json_dump = json.dumps(json_data)
print("json_string :: ", json_dump)
print("json_data tpye :: ", type(json_dump))

#json load
#dictironary를 json으로 변환
#타입 에러 TypeError: the JSON object must be str, bytes or bytearray, not dict
#json_load = json.loads(json_data)

json_load = json.loads(json_dump)
print("json_load :: ", json_load)
print("json_load type :: ", type(json_load))


'''
json_data ::  {'name': 'John', 'age': 30}
json_data type ::  <class 'dict'>
json_string ::  {"name": "John", "age": 30}
json_data tpye ::  <class 'str'>
json_load ::  {'name': 'John', 'age': 30}
json_load type ::  <class 'dict'>
'''

#json string은 ""로 나타낸다. dict는 ''로 나타나는 것을 확인할 수 있다.
