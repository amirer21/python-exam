def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list of float): A list of numbers to calculate the average for.

    Returns:
        float: The average of the input numbers.

    Raises:
        ValueError: If the input list is empty.

    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Input list is empty. Please provide a list of numbers.")
    
    total = sum(numbers)
    average = total / len(numbers)
    return average


#docstring(독스트링) : 코드 문서화

# "코드에 대한 문서화는 중요하다."
# 코드를 작성한 사람이 아닌 다른 사람이 코드를 읽고 이해할 수 있도록 문서화를 해야 한다.
# 혼자 만들고 혼자 사용하는 코드라면 문서화를 하지 않아도 될 수도 있으나, 대부분은 협업으로 개발하고, 협업하지 않았더라도 언젠가는 코드가 다른 개발자에게도 공유 때문에 문서화를 해야 한다.


# "코드를 분석하는데는 시간이 많이 소요된다."
# 문서화를 하지 않으면, 코드를 읽는 사람이 코드를 이해하기 위해 코드를 분석해야 한다. 코드를 분석하는데는 시간이 많이 소요된다.
# 그리고 내가 작성한 코드를 나중에 다시 보더라도, 문서화를 해놓지 않으면, 내가 작성한 코드를 이해하기 위해 코드를 분석해야 한다.
# 개발자가 퇴사하고 다른 개발자가 코드를 유지보수해야 할 때, 문서화를 해놓지 않으면, 또 다른 개발자가 코드를 이해하기 위해 코드를 분석해야 한다.
# 그리고 문서화가 잘 되어있는 코드는 다른 개발자로부터 질문으로 인한 시간 소요도 줄어들어서 나에게도 이점이 있다.
# 따라서, 코드에 대한 문서화는 중요하다. 필수적이다.

# 하지만, 문서화를 하지 않는 이유 대부분의 이유는, 코드를 작성하는 것만으로도 시간이 많이 소요되기 때문이다.
# 문서화 하지 않는 경우가 많다.

# 파이썬에서는 간단하게 코드에 대한 문서화를 할 수 있는 방법을 제공한다.
# 그리고, IDE에서 주석 작성 자동완성 기능까지 제공되기 때문에, 많은 시간을 들일필요없이 문서화를 할 수 있는 환경이 잘 갖추어져 있다.

# 파이썬에서는 docstring(독스트링)을 사용하여 코드에 대한 문서화하는 방법을 알아보자.
# docstring은 함수, 클래스, 모듈 등의 첫 번째 명령문으로 사용되는 문자열이다.
# 예를 들어, 아래와 같이 함수를 정의하고, 함수에 대한 설명을 docstring으로 작성할 수 있다.
# 파이썬에서 주석은 """ 을 사용한다.
# def calculate_average(numbers):
#     """
#     Calculate the average of a list of numbers.
#     Args:
#         numbers (list of float): A list of numbers to calculate the average for.
#     Returns:
#         float: The average of the input numbers.
#     Raises:
#         ValueError: If the input list is empty.
#     Example:
#         >>> calculate_average([1, 2, 3, 4, 5])
#         3.0
#     """
#     if not numbers:
#         raise ValueError("Input list is empty. Please provide a list of numbers.")
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average
#

#파이썬에서 이런 docstring을 문서화하는 방법은 여러가지가 있다.
#1. sphinx
#2. pdoc
#3. pydoc
#4. doxygen
#5. epydoc

# 이 중에서 sphinx를 사용해보자.
# sphinx는 파이썬 문서화를 위한 도구이다.
# docstring을 읽어서 html 문서로 만들어준다.

# 진행 순서
# 1. 코드에 docstring 작성
# 2. sphinx 설치
# 3. docs 폴더 생성
# 4. sphinx-quickstart
# 5. conf.py 설정
# 6. index.rst 설정
# 7. make html
# 8. 결과 확인


#설치
# pip install sphinx

# Sphinx 테마 설치 (선택사항)
#pip install sphinx-rtd-theme

# docs 폴더 생성
# 프로젝트 루트 폴더 아래에 docs 폴더를 생성한다.

#Quick Start
# 명령어 : sphinx-quickstart

# 프로젝트 구조
# docstringExam
# ├── _build : html 문서가 생성되는 폴더 <--- (결과) 여기에 html 문서가 생성된다. : _build\html\index.html
# ├── _static : css, js, image 등의 정적 파일을 저장하는 폴더
# ├── _templates : html 템플릿을 저장하는 폴더
# ├── docs : 문서화를 위한 파일들을 저장하는 폴더
# ├── conf.py : sphinx 설정 파일
# ├── index.rst : 문서의 시작점이 되는 파일. .rst 확장자는 reStructuredText의 약자이다. reStructuredText는 sphinx에서 사용하는 문서 작성 언어이다.
# └── make.bat : windows에서 html 문서를 생성하는 파일
# └── Makefile : linux에서 html 문서를 생성하는 파일
# └── doc_exam01.py : docstring을 작성할 파일 <--- (작성한 소스코드) 여기에 docstring을 작성하면 된다.




#conf.py 설정

#sphinx.ext.napoleon : Google Style docstring 사용시 파싱을 해주는 extensions이다.
#sphinx.ext.todo : Google Style docstring 사용시 Todo: 라고 적은 부분을 변환해줌. todo_include_todos=True값도 세트로 같이 설정해야 한다.
#sphinx.ext.autodoc : 모듈을 자동으로 문서화해주는 extensions이다.

# conf.py 파일에 아래와 같이 경로를 추가해준다.
# 만약 sphinx-apidoc 명령어를 실행 시, 경로 문제로 에러가 발생한다면, conf.py 파일에 아래와 같이 경로를 추가해준다.
# sys.path.insert("0", os.path.abspath("경로")) : 0번째 인덱스에 경로를 추가한다.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
'''
# Add your Python file path
import os
import sys
#sys.path.insert(0, os.path.abspath('../path/to/your/python/file'))
#docstring으로 작성할 코드의 절대 경로 D:\python_workspace\python-exam\docstringExam\doc_exam01.py
#프로젝트 경로 D:\python_workspace\python-exam\docstringExam
# 이렇게 한다. sys.path.insert(0, os.path.abspath('D:/python_workspace/python-exam/docstringExam'))
'''

#extensions 설정 
# sphinx.ext.autodoc 추가 : 모듈을 자동으로 문서화해주는 extensions이다.
'''
extensions = [
    'sphinx.ext.autodoc',
    # ... other extensions
]
'''
## exclude_patterns 설정 : 문서화하지 않을 파일을 설정한다.
#exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

## 테마 설정

#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'

#index.rst 설정


#Make html
# 명령어 : Make html
#\docstringExam\_build\html\index.html

# sphinx-apidoc 명령어 : 모듈을 자동으로 문서화해주는 명령어이다.
# sphinx-apidoc -f -o source/ ../path/to/your/python/file
# -f : 기존에 생성된 파일을 덮어쓰기
# -o : 문서화한 파일을 저장할 경로
# ../path/to/your/python/file : 문서화할 파일의 경로
# sphinx-apidoc -f -o docs/source D:\python_workspace\python-exam\docstringExam02  --separate


#참고 
## https://python-guide-kr.readthedocs.io/ko/latest/writing/documentation.html