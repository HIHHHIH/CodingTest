from copydetect import CopyDetector
from pathlib import Path
import numpy as np
import time
import os
from os.path import join

TESTS_DIR = str(Path(__file__).parent)

class CopyDetect():

    def __init__(self,user_id,problem_id,code,reference,boilerplate):
        self.user_id = user_id ## 유저 id
        self.problem_id = problem_id ## 문제 id
        self.code = code ## test할 코드 (string)
        self.reference = reference ## 다른 유저 제출 코드 (string list)
        self.boilerplate = boilerplate ## skeleton 코드 (string)
        return

    def setup(self):
        ## Date_user_id_problem_id
        current_time = int(time.time())
        self.dir_name = str(current_time) + "_" + str(self.user_id) + "_" + str(self.problem_id) ## 디렉토리 명 : (Unix timestamp)_(유저id)_(문제id)
        self.code_dir = join(TESTS_DIR,self.dir_name,"code") ## ~/dir_name/code
        self.reference_dir = join(TESTS_DIR,self.dir_name,"reference") ## ~/dir_name/reference
        self.boilerplate_dir = join(TESTS_DIR,self.dir_name,"boilerplate") ## ~/dir_name/boilerplate

        os.mkdir(join(TESTS_DIR,self.dir_name))
        os.mkdir(self.code_dir)
        os.mkdir(self.reference_dir)
        os.mkdir(self.boilerplate_dir)

        # dir_name
        #  |_code
        #  |_reference
        #  |_boilerplate 

        with open(join(self.code_dir,'test.py'),'w') as t: ## 표절 test code 파일 생성
            t.write(self.code)
            t.close()
        
        for index ,i in enumerate(self.reference): ## 다른 유저 제출 코드 파일들 생성
            with open(join(self.reference_dir,"{0}.py".format(index)), 'w') as r:
                r.write(i)
                r.close()

        with open(join(self.boilerplate_dir,'boilerplate.py'),'w') as b: ## skeleton code 파일 생성
            b.write(self.boilerplate)
            b.close()

        # dir_name
        #   |_code
        #       |_test.py
        #   |_reference
        #       |_0.py
        #       |_1.py
        #       |_2.py
        #           .
        #           .
        #           .
        #   |_boilerplate
        #       |_boilerplate.py
        # 
        return

    def teardown(self): ## 생성한 파일, 디렉토리 삭제
        for i in os.listdir(self.code_dir):
            os.remove(join(self.code_dir,i))
        
        for i in os.listdir(self.reference_dir):
            os.remove(join(self.reference_dir,i))

        for i in os.listdir(self.boilerplate_dir):
            os.remove(join(self.boilerplate_dir,i))

        os.rmdir(self.code_dir)
        os.rmdir(self.reference_dir)
        os.rmdir(self.boilerplate_dir)
        os.rmdir(join(TESTS_DIR,self.dir_name))

        return

    def run_detector(self): ## copy detect run
        if len(self.reference) == 0:
            return {
                "plagiarism_rate" : 0
            }
        config = {
          "test_directories" : [self.code_dir],
          "reference_directories" : [self.reference_dir],
          "boilerplate_directories" : [self.boilerplate_dir],
          "extensions" : ["py"], ## 확장자 명
          "noise_threshold" : 25, ## 
          "guarantee_threshold" : 25, ##
          "display_threshold" : 0,
          "disable_autoopen" : True,
        }
        detector = CopyDetector.from_config(config)
        detector.run()

        cp_code_list = detector.get_copied_code_list()
        plagiarism_rates = []
        for i in cp_code_list:
            plagiarism_rates.append(i[0])
        
        result_rate = 0
        if len(plagiarism_rates) > 0:
            result_rate = max(plagiarism_rates)
        
        copydetect_result = {
            "plagiarism_rate" : result_rate
        }

        return copydetect_result