import os
import json


def multimetric_run(user_code):
    # user_code: string -> file(.py)
    temp_file = open('./user_code.py', 'w')
    temp_file.write(user_code)
    temp_file.close()

    # result file saved as /CodingTest/back/multimetric_result.json
    os.system("multimetric ./user_code.py > multimetric_result.json")

    with open('./multimetric_result.json', 'r') as result:
        data = json.load(result)

    # parse the result
    halstead = data['overall']['halstead_timerequired']
    loc = data['overall']['loc']
    control_complexity = data['overall']['cyclomatic_complexity']
    data_complexity = data['overall']['operands_uniq']

    # remove the temporary file
    if os.path.isfile('./user_code.py'):
        os.remove('./user_code.py')
    if os.path.isfile('./multimetric_result.json'):
        os.remove('./multimetric_result.json')

    return halstead, loc, control_complexity, data_complexity
