import sys
import traceback
from io import StringIO

def execute(code):
    is_success = False
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code)
        sys.stdout = old_stdout
        line_number = None
        is_success = True
        return is_success, line_number, redirected_output.getvalue()
    except SyntaxError as err:
        sys.stdout = old_stdout
        message = message = traceback.format_exc(limit=0)
        cl, exc, tb = sys.exc_info()
        line_number = err.lineno
    except Exception as err:
        sys.stdout = old_stdout
        message = traceback.format_exc(limit=0)
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    else:
        return
    return is_success, line_number, message


