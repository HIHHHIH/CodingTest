import unittest
import os
import sys
import string
import random

'''
run_test(user_code, input, output) 으로 테스트실행. 파라미터는 run_test 주석 참고.
'''
#둘 다 1,2,3,4,5를 키로 하는 딕셔너리
result_list = {}  #모든 테스트 결과 저장
output_list = {}  #모든 유저 아웃풋 저장


def rand_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


class CaseTester(unittest.TestCase):
    solution = None
    params = ()
    outputs = None

    def setUp(self):  # 각 테스트 전마다 자동 실행
        self.test_num = int(self.id()[-1]) - 1  # 테스트케이스번호

    def tearDown(self):  #각 테스트 후마다 자동 실행
        global result_list

        if hasattr(self._outcome, 'errors'):  #파이선 버전에 따라 결과 호출 방식이 다름.
            # Python 3.4 - 3.10  (These two methods have no side effects)
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        else:
            # Python 3.11+
            result = self._outcome.result

        ok = all(test != self for test, text in result.errors + result.failures)
        if ok:  #테스트 통과하면 'P'로 저장
            result_list[self.test_num] = 'P'
        else:
            error = any(test == self for test, text in result.errors)
            if error:  #실행 오류면 'E'로 저장
                result_list[self.test_num] = 'E'
            else:  #아웃풋이 틀리면 'F'로 저장
                result_list[self.test_num] = 'F'

    def test_case1(self):  #test_로 시작하는 method는 unittest.main()실행하면 알아서 테스트함.
        global output_list
        try:
            user_output = self.solution(*self.params[self.test_num])
        except Exception as e:
            user_output = 'Error'
        output_list[self.test_num] = user_output
        self.assertEqual(user_output, self.outputs[self.test_num])

    def test_case2(self):
        global output_list
        try:
            user_output = self.solution(*self.params[self.test_num])
        except Exception as e:
            user_output = 'Error'
        output_list[self.test_num] = user_output
        self.assertEqual(user_output, self.outputs[self.test_num])

    def test_case3(self):
        global output_list
        try:
            user_output = self.solution(*self.params[self.test_num])
        except Exception as e:
            user_output = 'Error'
        output_list[self.test_num] = user_output
        self.assertEqual(user_output, self.outputs[self.test_num])

    def test_case4(self):
        global output_list
        try:
            user_output = self.solution(*self.params[self.test_num])
        except Exception as e:
            user_output = 'Error'
        output_list[self.test_num] = user_output
        self.assertEqual(user_output, self.outputs[self.test_num])

    def test_case5(self):
        global output_list
        try:
            user_output = self.solution(*self.params[self.test_num])
        except Exception as e:
            user_output = 'Error'
        output_list[self.test_num] = user_output
        self.assertEqual(user_output, self.outputs[self.test_num])

def run_test(mode ,user_code, input, output, file_name):
    """

    :param user_code: 유저가 작성한 코드, string
    :param input: 모든 테스트케이스의 인풋 리스트 ex) (1,3,5,6,7) or ((2,1),(4,6),(11,6),(0,6),(1,3))
    :param output: 모든 테스트케이스의 아웃풋 리스트 ex) (4,6,7,8,9) or (True, True, False, False,True)
    :return: 모든 테스트 결과를 모은 Dictionary. key= 케이스번호, value= 통과여부 ex) {'1':'P','2':'P','3':'F','4':'P','5':'F'}
    """

    with open(file_name + '.py', 'w') as f:
        # solution()을 static method로 만들어서 self argument를 필요로 하지 않도록 함.
        f.write("@staticmethod\n")
        f.write(user_code)
        f.close()

    mod_name = file_name
    temp_code = __import__('%s' % (mod_name), fromlist=[mod_name])  #동적 임포트
    CaseTester.params = input
    try:
        CaseTester.solution = temp_code.solution
    except Exception as e:
        return [{'result': 'skeleton_error', 'detail': 'the method name should be solution.'}, {}, {}]
    CaseTester.outputs = output

    suite = unittest.TestSuite()
    if mode == 'whole':
        suite.addTest(CaseTester("test_case1"))  # 테스트 케이스 하나씩 추가
        suite.addTest(CaseTester("test_case2"))
        suite.addTest(CaseTester("test_case3"))
        suite.addTest(CaseTester("test_case4"))
        suite.addTest(CaseTester("test_case5"))
    elif mode == 'single':
        suite.addTest(CaseTester("test_case1"))
    else:
        return [{'result':'mode_error','detail':'mode should be either "single" or "whole".'},{},{}]

    runner = unittest.TextTestRunner()
    runner.run(suite)

    os.remove(file_name+'.py')  # 임시 저장한 유저코드 파일 삭제

    return [{'result':'ok'}, result_list, output_list]

''' run_test에 통합함.
def run_specific_test(user_code, input, output, file_name):
    """run_test의 수정버전
        test case 1개만 선택해서 할 때 사용
    """

    with open(file_name + '.py', 'w') as f:
        f.write("@staticmethod\n")
        f.write(user_code)
        f.close()

    mod_name = file_name
    temp_code = __import__('%s' % (mod_name), fromlist=[mod_name])  # 동적 임포트
    CaseTester.params = input
    CaseTester.solution = temp_code.solution
    CaseTester.outputs = output

    suite = unittest.TestSuite()
    suite.addTest(CaseTester("test_case1"))  # 테스트 케이스 하나씩 추가
    runner = unittest.TextTestRunner()
    runner.run(suite)

    os.remove(file_name+'.py')  # 임시 저장한 유저코드 파일 삭제

    return [result_list, output_list]
'''

if __name__ == '__main__':
    user_code = "def solution(a,b,c):\n\ta+=1\n\treturn a+b+c"  #실행예시
    # 두번째, 다섯번째에서 오류발생하게 해놓음

    print(run_test(user_code,[[1,2,3],[2,3,4],[3,4,5],[4,5,6],[7,8,9]], [7,15,13,16,21])) # [user_code, input(list or tuple), output)
