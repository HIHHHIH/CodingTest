import unittest
import os

'''
case_tester.py를 실행해서 테스트가 작동하는 것을 확인할 수 있음.
실행 도중 에러가 발생하면 E, 아웃풋이 틀리면 F을 프린트함.
'''


class CaseTester(unittest.TestCase):
    user_class = None
    params = ()
    outputs = None
    def setUp(self): # 각 테스트 전마다 자동 실행
        pass

    def tearDown(self):  #각 테스트 후마다 자동 실행
        pass

    def test_case1(self):  #test_로 시작하는 method는 unittest.main()실행하면 알아서 테스트함.

        user_output = self.user_class.solution(*self.params[0])
        self.assertEqual(user_output, self.outputs[0])

    def test_case2(self):

        user_output = self.user_class.solution(*self.params[1])
        self.assertEqual(user_output, self.outputs[1])

    def test_case3(self):

        user_output = self.user_class.solution(*self.params[2])
        self.assertEqual(user_output, self.outputs[2])

    def test_case4(self):

        user_output = self.user_class.solution(*self.params[3])
        self.assertEqual(user_output, self.outputs[3])

    def test_case5(self):

        user_output = self.user_class.solution(*self.params[4])
        self.assertEqual(user_output, self.outputs[4])

def run_test(user_code, input, output):
    """
    unittest에서 사용가능한 형태로 usercode를 수정해서 로컬에 임시 저장함.
    solution() 상위에 class를 놓고, solution 첫 파라미터로 self를 넣음
    """

    with open("temp_code2.py", 'w') as f:
        f.write("class UserCode:\n\t")
        for line in user_code.splitlines():
            idx = line.find("solution(")
            if idx != -1:
                line = line[:idx+9] + "self, " + line[idx+9:]
            f.write("\n\t" + line)
        f.close()

    import temp_code2
    CaseTester.params = input
    CaseTester.user_class = temp_code2.UserCode()
    CaseTester.outputs = output
    unittest.main()
    os.remove("temp_code2.py")  # 임시 저장한 유저코드 파일 삭제
    print('hello')


if __name__ == '__main__':
    user_code = "def solution(a,b,c):\n\ta+=1\n\treturn a+b+c"  #실행예시
    # 세번째, 다섯번째에서 오류발생하게 해놓음
    run_test(user_code,[[1,2,3],[2,3,4],[3,4,5],[4,5,6],[7,8,9]], [7,15,13,16,21]) # [user_code, input(list or tuple), output)





