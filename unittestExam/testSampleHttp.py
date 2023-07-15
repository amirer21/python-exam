import unittest

#test target function
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
    
    def chkResponse(self, x, y):
        if x == y:
            return True
        else:
            return False        
        
    
    def chkTextResponse(self, x, y):
        if x == y:
            return True
        else:
            return False        
        


# unittest.TestCase를 상속받아 테스트
class ApiFunctionsTest(unittest.TestCase):

    def setUp(self):
        # Create an instance of ApiFunctions for each test case
        self.apiTestTarget = ApiFunctions()

    def tearDown(self):
        # Clean up resources if needed
        pass

    def test_getMethod(self):
        result = self.apiTestTarget.getMethod("apiUrl", "testQuery")
        self.assertEqual(result, 200)

    def test_postMethod(self):
        result = self.apiTestTarget.postMethod("apiUrl", "testQuery")
        self.assertEqual(result, 433)
        
    def test_chkResponse(self):
        result = self.apiTestTarget.chkResponse("apiTest", "apiTest")
        self.assertEqual(result, True)
        
    def test_chkTextResponse(self):
        result = self.apiTestTarget.chkTextResponse("abc", "def")
        self.assertEqual(result, True)


# Run the tests
if __name__ == '__main__':
    unittest.main()
