import sys
import traceback
from io import StringIO

class InterpreterError(Exception): pass

def execute(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code)
        sys.stdout = old_stdout
        return redirected_output.getvalue()
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        error_class = err.__class__.__class__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    else:
        return
    description = ("%s at line %d of your code\n%s: %s" % (error_class, line_number, code, detail))
    return description


