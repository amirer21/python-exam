import pytest, sys, logging 
from time import sleep
import os
import sys
#path = os.path.join(os.path.dirname(__file__), os.pardir)
path = 'D:/python_workspace/pythonExam/unittestproject'
sys.path.append(path)
from apiConnector import CRUDConnector, SoftwareTest, SoftwareCategory, ApiFunctions
#pip3 install pytest-html 
#pytest --html=report/report.html 실행하려는파일.py

#코드 전체 참고 https://kibua20.tistory.com/227

# 코드 https://docs.pytest.org/en/latest/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization

#test_라는 접두사(Prefix)로 시작하는 파일 또는 _test라는 접미사(Suffix)로 끝나는 파일을 찾아서 테스트 코드를 실행하고 그 결과를 화면에 출력
#pytest만 실행했을 때 자동으로 파일을 찾아서 테스트 코드를 실행
#https://wikidocs.net/80337

#참고
#fixtures https://docs.pytest.org/en/7.4.x/reference/fixtures.html#fixtures
#skip https://docs.pytest.org/en/7.1.x/how-to/skipping.html
#pytest html report https://pytest-html.readthedocs.io/en/latest/user_guide.html
#pytest option https://docs.pytest.org/en/6.2.x/reference.html#command-line-flags
#pytest.ini https://pytest-with-eric.com/pytest-best-practices/pytest-ini/

#Structure
#Test code는 기존 프로젝트 코드와 다른 디렉토리에 위치하도록 하였다.
# pytest.ini : pytest 실행시 필요한 설정을 기술.  CLI 명령을 사용하여 테스트를 실행할 때마다 테스트 작동 방식을 지정해야되는데 이를 pytest.ini 파일에 기술하여 테스트 실행시마다 옵션을 입력하지 않아도 되도록 한다.
# conftest.py : html report를 생성하기 위한 설정을 기술
# test_pytestsample.py : pytest 테스트 코드를 기술


# ------------------------------------------------------------------------------------------
# Test 1. 함수별(Function Test)
# ------------------------------------------------------------------------------------------
'''fixture test case 함수를 실행 "전"에 실행'''

def setup_function(function):    
    #logging.info 옵션
    #sys._getframe(n) : n단계 전의 프레임을 얻음
    #sys._getframe(0).f_code.co_name : 현재 실행중인 함수 이름 구하기
    #sys._getframe(n).f_locals을 이용하여 해당 프레임의 지역 변수도 접근 가능
    logging.info(sys._getframe(0).f_code.co_name) 
    
    
'''teardown test case 함수를 실행 "후"에 실행'''
def teardown_function(function):
    logging.info(sys._getframe(0).f_code.co_name)


'''assert() 테스트 성공, 실패 판단'''
def test_function_01():
    """ Test Function"""
    logging.info(sys._getframe(0).f_code.co_name)
    assert (True)

def test_function_02():
    """ Test Function"""
    logging.info(sys._getframe(0).f_code.co_name)
    assert (True)


# ------------------------------------------------------------------------------------------
# Test 2. 클래스(Class Test)
# ------------------------------------------------------------------------------------------
class TestClassSample():   
    
    #@pytest.fixture 이 어노테이션을 사용하면, 테스트 실행 전에 이 함수를 실행하여 값이나 리소스에 필요한 준비 작업을 할 수 있다.
    @pytest.fixture
    def serial_tester(self):
        logging.info(sys._getframe(0).f_code.co_name)
        return CRUDConnector()    
    
    @pytest.fixture(autouse=True) #클래스 내의 모든 테스트 메서드에서 픽스처가 자동으로 사용
    def setUp(self):        
        self.apiTestTarget = ApiFunctions()
    
    @pytest.fixture
    def post_serial(self, serial_tester):
        logging.info(sys._getframe(0).f_code.co_name)
        tester = serial_tester.create_serial()
        yield tester
        serial_tester.delete_serial(tester)
        
    @pytest.fixture
    def get_serial(self, serial_tester):
        logging.info(sys._getframe(0).f_code.co_name)
        tester = serial_tester.create_serial()
        yield tester
        tester.clear_serial()
        serial_tester.delete_serial(tester)    
    
    #assert 테스트 성공, 실패 판단
    def test_serial_get(self, post_serial, get_serial):
        logging.info(sys._getframe(0).f_code.co_name)
        serial = SoftwareCategory(name='test', version='1.0')
        post_serial.send_serial(serial, get_serial)        
        assert serial in get_serial.category
        
    def test_getMethod_pass(self):
        logging.info(sys._getframe(0).f_code.co_name)
        result = self.apiTestTarget.getMethod("apiUrl", "testQuery")
        assert result == 200
        
    def test_getMethod_fail(self):
        logging.info(sys._getframe(0).f_code.co_name)
        result = self.apiTestTarget.getMethod("apiUrl", "testQuery")
        assert result == 500

    def test_postMethod(self):
        logging.info(sys._getframe(0).f_code.co_name)
        result = self.apiTestTarget.postMethod("apiUrl", "testQuery")
        assert result == 433
    
    # @classmethod : 클래스 메서드 사용하며, cls 키워드를 사용한다. (self 와의 차이 : self는 인스턴스 메서드)
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which usually contains tests)."""
        logging.info(sys._getframe(0).f_code.co_name)
        cls.name= 'test'
        cls.members = [1, 2, 3, 4]        

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to setup_class."""
        logging.error(sys._getframe(0).f_code.co_name)
        pass
        

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a class.  
        setup_method is invoked for every test method of a class.
        """
        logging.info(sys._getframe(0).f_code.co_name)

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method call.
        """
        logging.info(sys._getframe(0).f_code.co_name)        


    def test_0001(self):
        logging.info(sys._getframe(0).f_code.co_name)
        sleep(1)
        assert (True)
        
    @pytest.mark.mandatory
    def test_mandatory(self):
        logging.info(sys._getframe(0).f_code.co_name)
        assert True

    '''특정 테스트 케이스를 skip'''
    #@pytest.mark.skip 는 테스트를 건너뛰도록 지정
    #https://docs.pytest.org/en/7.1.x/how-to/skipping.html
    @pytest.mark.skip("Do not run this testcase")
    def test_fail():
        assert False
       
    # reason은 테스트를 건너뛰는 이유를 설명하는 문자열
    @pytest.mark.skip(reason="Skip reasson")
    def test_0002(self):
        logging.info(sys._getframe(0).f_code.co_name)
        sleep(1)
        assert (True)
    
    # skipif()는 조건부로 무언가를 건너뛰도록 지정
    testData = None    
    @pytest.mark.skipif(testData is None, reason="testData is None")
    #@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
    def test_chkTestData():
        assert (True)                

    def test_0003(self):
        logging.info(sys._getframe(0).f_code.co_name)
        sleep(1)
        assert (False)


# pytest_sessionfinish : 테스트 세션을 끝낼 때 호출
class MyPlugin:
    def pytest_sessionfinish(self):
        pass


if __name__ == "__main__":
    # args_str = '--html=report/report.html --self-contained-html '+ __file__
    # args_str = ' --capture=tee-sys '+ __file__
    args_str = '--html=report/report.html ' + __file__ # html report 생성
    args = args_str.split(" ")
    
    pytest.main(args, plugins=[MyPlugin()]) # 플러그인 추가
    # pytest.main(args)