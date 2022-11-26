#-*- coding:utf-8 -*-

from pylama.main import parse_options, check_paths
import os

def pylama_run(file_name):
    # set pylama options
    my_path = '.' # \CodingTest\back
    linters = ['mypy', 'pylint', 'eradicate', 'radon', 'pycodestyle']
    file_list = os.listdir(my_path) # 현재 폴더의 모든 파일 목록
    file_list.remove(file_name) # 테스트 대상 파일만 제외
    skip_list = ','.join(file_list)
    my_redefined_options = {
        'linters': linters,
        'skip': skip_list
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
        if (e.etype != 'N'):
            if pylama_result[e.source]["score"] > 0: # 감점
                pylama_result[e.source]["score"] -= 1
                pylama_result[e.source]["msg"].append("Line "+str(e.lnum)+": "+e.message) # add message to list
    return pylama_result

"""
5개 평가 항목, 각 20점 만점, 감점제, 메시지 최대 20개
result example
{
    'mypy': {
        'score': 19, 
        'msg': [
            'Line 3: Skipping analyzing "pylama.main": module is installed, but missing library stubs or py.typed marker'
            ]
    }, 
    'pylint': {
        'score': 14, 
        'msg': [
            'Line 1: Missing module docstring', 
            'Line 4: standard import "import os" should be placed before "from pylama.main import parse_options, check_paths"', 
            'Line 6: Missing function or method docstring', 'Line 44: Variable name "e" doesn\'t conform to snake_case naming style', 
            "Line 45: Unnecessary parens after 'if' keyword", 'Line 51: Final newline missing'
            ]
    }, 
    'eradicate': {
        'score': 20, 
        'msg': []
    }, 
    'radon': {
        'score': 20, 
        'msg': []
    }, 
    'pycodestyle': {
        'score': 7, 
        'msg': [
            "Line 1: block comment should start with '# '", 
            'Line 6: expected 2 blank lines, found 1', 
            'Line 8: at least two spaces before inline comment', 
            'Line 10: at least two spaces before inline comment', 
            'Line 11: at least two spaces before inline comment', 
            'Line 46: at least two spaces before inline comment', 
            'Line 48: line too long (111 > 100 characters)', 
            'Line 48: missing whitespace around arithmetic operator', 
            'Line 48: missing whitespace around arithmetic operator', 
            'Line 48: missing whitespace around arithmetic operator', 
            'Line 48: at least two spaces before inline comment', 
            'Line 51: no newline at end of file', 
            'Line 51: expected 2 blank lines after class or function definition, found 0'
            ]
    }
}
"""