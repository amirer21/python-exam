# DTO(Data Transfer Object) : 데이터 전송 객체
# DTO는 계층간 데이터 교환을 위한 자바빈즈를 의미하는 용어로 사용되었다.
# DTO는 로직을 갖고 있지 않는 순수한 데이터 객체이며, getter/setter 메소드만을 갖는다.

# 다음은 기본적인 DTO의 예이다.
# 파이썬에서는 속성 접근 제어를 위해 getter/setter 메소드를 명시적으로 정의하지 않는다.
# 파이썬에서는 속성 시스템을 사용하여 속성에 접근하는 방식을 제어한다.
class UserDTO:
    # __init__ : 생성자
    # self : 자기 자신을 가리키는 참조자
    # self.username : 인스턴스 변수
    # 파이썬에서 __init__은 생성자로 사용되며, 클래스의 인스턴스가 만들어질 때 한 번만 호출된다.
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    # 파이썬에서 __str__은 객체를 문자열로 표현할 때 사용한다.
    def __str__(self):
        return f'UserDTO(username={self.username}, email={self.email})'

# Usage
user_data = UserDTO(username='john_doe', email='john@example.com')
print(user_data)

########
## 파이썬 Getter, Setter 예제
# 파이썬에서는 getter/setter 메소드를 일반적인 메소드 형태가 아닌, 데코레이터를 사용하여 메소드를 정의한다.
class UserDTO:
    def __init__(self, username, email, value):
        self._username = username
        self._email = email
        self._value = None
    
    #@property : getter
    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email
    
    @property
    def value(self):
        return self._value

    @value.setter
    def add_value(self, new_value):
        self._value = new_value    

# 클래스 내부에 정의된 메소드는 첫 번째 인자로 항상 인스턴스 자신을 가리키는 self를 전달받는다.
# 클래스를 생성하고, 인스턴스 변수에 접근하려면 인스턴스를 생성해야 한다.
# UserDTO 크래스의 인스턴스를 생성하고, 인스턴스 변수에 접근해보자.
# 매개변수에 값을 전달하지 않으면, 기본값으로 None이 할당된다.
# 여기서 user_data는 UserDTO 클래스의 인스턴스이다.
user_data = UserDTO(username='john_doe', email='john@example.com', value=None)

# getter
# 인스턴스에서 값 가져오기
# 각각의 인스턴스 변수에 접근하기 위해서는 인스턴스 변수 앞에 점(.)을 붙여야 한다.
# 인스턴스 변수에 접근하는 방법은 다음과 같다.
print(user_data.username) 
print(user_data.email)

# setter
# 인스턴스 변수에 값 할당이 되지 않았기 때문에, getter로 정의된 메소드를 호출하면 None이 출력된다.
print(obj.value)  # Output: None

## setter로 정의된 메소드(add_value)를 호출하면, 인스턴스 변수에 값을 할당할 수 있다.
obj.add_value = 42  
print(obj.value)  # Output: 42

