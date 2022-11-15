from pylama.main import parse_options, check_paths
import os

def pylama_run(user_code):
    file_list = os.listdir('.') # 현재 폴더의 모든 파일 목록
    skip_list = ','.join(file_list) 
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
        'skip': skip_list
    }
    my_path = '.' 

    # save .py file into this directory
    my_file = my_path + "\\user_code.py"
    f = open(my_file, "w")
    f.write(user_code)

    # run pylama
    options = parse_options([my_path], **my_redefined_options)
    errors = check_paths(my_path, options, rootdir='.')
    for e in errors:
        if pylama_result[e.source][0] > 0: # 감점
            pylama_result[e.source][0] -= 1
        pylama_result[e.source].append(e.message) # add message to list
    
    # delete .py file
    f.close()
    if os.path.isfile(my_file):
        os.remove(my_file)

    return pylama_result
# {"mypy": [20, msg1, msg2, ...],"pylint": [20, msg1, msg2, ...],"eradicate": [20, msg1, msg2, ...],"radon": [20, msg1, msg2, ...],"pycodestyle": [20, msg1, msg2, ...]}
