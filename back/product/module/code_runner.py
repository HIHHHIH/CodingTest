import sys
import traceback
from io import StringIO

def execute(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code)
        sys.stdout = old_stdout
        return redirected_output.getvalue()
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
    return line_number, message


