import os
import sys

#path = os.path.join(os.path.dirname(__file__), os.pardir)
path = 'D:/python_workspace/insta/unittestproject'
sys.path.append(path)

#DTO 클래스
class SoftwareCategory:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        
                
class CRUDConnector:
    def create_serial(self):
        return SoftwareTest()

    def delete_serial(self, tester):
        # do some cleanup
        pass


class SoftwareTest:
    def __init__(self):
        self.category = []

    def send_serial(self, serial, software):
        software.category.append(serial)

    def clear_serial(self):
        self.category.clear()


class ApiFunctions:
    def getMethod(self, x, y):
        if x == "apiUrl" and y == "testQuery":
            return 200
        else:
            return 400
        
    def postMethod(self, x, y):
        if x == "apiUrl" and y == "testQuery":
            return 433
        else:
            return 400