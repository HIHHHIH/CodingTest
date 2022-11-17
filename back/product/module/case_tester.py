import unittest
import os
import sys

'''
run_test(user_code, input, output) 으로 테스트실행. 파라미터는 run_test 주석 참고.
'''

test_results = {}  #모든 테스트 결과 저장
temp_output = {}  #모든 유저 아웃풋 저장

class CaseTester(unittest.TestCase):
    user_class = None
    params = ()
    outputs = None

    def setUp(self):  # 각 테스트 전마다 자동 실행
        pass

    def tearDown(self):  #각 테스트 후마다 자동 실행
        global test_results

        if hasattr(self._outcome, 'errors'):  #파이선 버전에 따라 결과 호출 방식이 다름.
            # Python 3.4 - 3.10  (These two methods have no side effects)
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        else:
            # Python 3.11+
            result = self._outcome.result

        test_num = int(self.id()[-1])  #테스트케이스번호

        ok = all(test != self for test, text in result.errors + result.failures)

        if ok:  #테스트 통과하면 'P'로 저장
            test_results[test_num] = 'P'
        else:  #테스트 실패하면 'F'로 저장
            test_results[test_num] = 'F'

    def test_case1(self):  #test_로 시작하는 method는 unittest.main()실행하면 알아서 테스트함.

        user_output = self.user_class.solution(*self.params[0])
        global temp_output
        temp_output[1] = user_output
        self.assertEqual(user_output, self.outputs[0])

    def test_case2(self):

        user_output = self.user_class.solution(*self.params[1])
        global temp_output
        temp_output[2] = user_output
        self.assertEqual(user_output, self.outputs[1])

    def test_case3(self):

        user_output = self.user_class.solution(*self.params[2])
        global temp_output
        temp_output[3] = user_output
        self.assertEqual(user_output, self.outputs[2])

    def test_case4(self):

        user_output = self.user_class.solution(*self.params[3])
        global temp_output
        temp_output[4] = user_output
        self.assertEqual(user_output, self.outputs[3])

    def test_case5(self):

        user_output = self.user_class.solution(*self.params[4])
        global temp_output
        temp_output[5] = user_output
        self.assertEqual(user_output, self.outputs[4])

def run_test(user_code, input, output):
    """

    :param user_code: 유저가 작성한 코드, string
    :param input: 모든 테스트케이스의 인풋 리스트 ex) (1,3,5,6,7) or ((2,1),(4,6),(11,6),(0,6),(1,3))
    :param output: 모든 테스트케이스의 아웃풋 리스트 ex) (4,6,7,8,9) or (True, True, False, False,True)
    :return: 모든 테스트 결과를 모은 Dictionary. key= 케이스번호, value= 통과여부 ex) {'1':'P','2':'P','3':'F','4':'P','5':'F'}
    """

    """
    unittest에서 사용가능한 형태로 usercode를 수정해서 로컬에 임시 저장함.
    solution() 상위에 class를 놓고, solution 첫 파라미터로 self를 넣음
    """
    with open("temp_code.py", 'w') as f:
        f.write("class UserCode:\n\t")
        for line in user_code.splitlines():
            idx = line.find("solution(")
            if idx != -1:
                line = line[:idx+9] + "self, " + line[idx+9:]
            f.write("\n\t" + line)
        f.close()

    import temp_code
    CaseTester.params = input
    CaseTester.user_class = temp_code.UserCode()
    CaseTester.outputs = output

    #unittest.main(exit=False)  #테스트 실행 오류남.

    # 다른 실행방법
    suite = unittest.TestSuite()
    suite.addTest(CaseTester("test_case1"))  # 테스트 케이스 하나씩 추가
    suite.addTest(CaseTester("test_case2"))
    suite.addTest(CaseTester("test_case3"))
    suite.addTest(CaseTester("test_case4"))
    suite.addTest(CaseTester("test_case5"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    os.remove("temp_code.py")  # 임시 저장한 유저코드 파일 삭제

    return [test_results, temp_output]


if __name__ == '__main__':
    user_code = "def solution(a,b,c):\n\ta+=1\n\treturn a+b+c"  #실행예시
    # 두번째, 다섯번째에서 오류발생하게 해놓음

    print(run_test(user_code,[[1,2,3],[2,3,4],[3,4,5],[4,5,6],[7,8,9]], [7,15,13,16,21])) # [user_code, input(list or tuple), output)




