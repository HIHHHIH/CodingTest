#-*- coding:utf-8 -*-

from pylama.main import parse_options, check_paths
import os

def pylama_run(file_name):
    # set pylama options
    my_path = '.' # \CodingTest\back
    linters = ['mypy', 'pylint', 'eradicate', 'radon', 'pycodestyle']    
    my_redefined_options = {
        'linters': linters
    }

    pylama_result = {
        "mypy": {
            "score": 20,
            "msg": []
        },
        "pylint": {
            "score": 20,
            "msg": []
        },
        "eradicate": {
            "score": 20,
            "msg": []
        },
        "radon": {
            "score": 20,
            "msg": []
        },
        "pycodestyle": {
            "score": 20,
            "msg": []
        }
    }

    # run pylama
    options = parse_options([my_path], **my_redefined_options)
    errors = check_paths(my_path, options, rootdir='.')
    for e in sorted(errors, key=lambda x: x.lnum):
        if e.filename == file_name and e.etype != 'N':
            if pylama_result[e.source]["score"] > 0: # 감점
                pylama_result[e.source]["score"] -= 1
                pylama_result[e.source]["msg"].append("Line "+str(e.lnum)+": "+e.message) # add message to list
    return pylama_result

"""
pylama에는 파이썬 코드의 가독성을 평가하는 여러 라이브러리들이 포함되어 있습니다.
우리는 개요 자료에 나온 5가지 라이브러리를 사용합니다. ['mypy', 'pylint', 'eradicate', 'radon', 'pycodestyle']
mypy: type checker
radon: Halstead metrics나 cyclomatic complexity 등 수치 높아서 결함 발생률 높은 부분 찾기
eradicate: 불필요한 주석
pylint, pycodestyle: coding style convention
각 라이브러리별로 20점 만점, 결함 하나당 1점씩 감점제, 각 최대 20개 메시지
"""