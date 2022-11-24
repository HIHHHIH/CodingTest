#-*- coding:utf-8 -*-

from pylama.main import parse_options, check_paths
import os
import pathlib

def pylama_run(file_name):
    # set pylama options
    my_path = str(pathlib.Path.cwd() / 'product' / 'views')
    linters = ['mypy', 'pylint', 'eradicate', 'radon', 'pycodestyle']
    file_list = os.listdir(my_path) # 현재 폴더의 모든 파일 목록
    file_list.remove(file_name) # 테스트 대상 파일만 제외 
    skip_list = ','.join(file_list)
    my_redefined_options = {
        'linters': linters,
        'skip': skip_list
    }

    pylama_result = {
        "mypy": [20, ],
        "pylint": [20, ],
        "eradicate": [20, ],
        "radon": [20, ],
        "pycodestyle": [20, ]
    }

    # run pylama
    options = parse_options([my_path], **my_redefined_options)
    errors = check_paths('.', options, rootdir=my_path)
    for e in errors:
        if (e.etype != 'N'):
            if pylama_result[e.source][0] > 0: # 감점
                pylama_result[e.source][0] -= 1
                pylama_result[e.source].append("Line "+e.lnum+": "+e.message) # add message to list
    return pylama_result
# {"mypy": [20, msg1, msg2, ...],"pylint": [20, msg1, msg2, ...],"eradicate": [20, msg1, msg2, ...],"radon": [20, msg1, msg2, ...],"pycodestyle": [20, msg1, msg2, ...]}
# 5개 평가 항목, 각 20점 만점, 감점제, 메시지 최대 20개
