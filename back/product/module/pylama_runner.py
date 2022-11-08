from pylama.main import parse_options, check_paths

def pylama_run(user_code):
    pylama_result = {
        "mypy": [20, ],
        "pylint": [20, ],
        "eradicate": [20, ],
        "radon": [20, ],
        "pycodestyle": [20, ]
    }
    linters = ['mypy', 'pylint', 'eradicate', 'radon', 'pycodestyle']
    my_redefined_options = {
        'linters': linters,
    }
    my_path = '.' # user_code
    # my_path: 상대경로. 지정 폴더 안에 있는 모든 .py 파일 검사 
    # user_code .py로 파일 저장 후 채점 가능한가요
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe4 in position 141: invalid continuation byte
    # /,\ 둘 다 발생 

    options = parse_options([my_path], **my_redefined_options)
    errors = check_paths(my_path, options, rootdir='.')
    for e in errors:
        if pylama_result[e.source][0] > 0: # 감점
            pylama_result[e.source][0] -= 1
        pylama_result[e.source].append(e.message) # add message to list

    return pylama_result