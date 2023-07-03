from typing import Dict,Optional
import logging_code
import sys
from io import StringIO
import os

class PythonREPL:
    """A class for running Python code in a REPL."""

    def __init__(self, _globals: Optional[Dict] = None, _locals: Optional[Dict] = None):
        self._globals = _globals if _globals is not None else {'os': os}
        self._locals = _locals if _locals is not None else {}


    def run(self, code: str) -> str:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        code = "import os\n" + code
        try:
            exec( code, self._globals, self._locals )
        finally:
            sys.stdout = old_stdout
        result = redirected_output.getvalue()
        logging_code.logger.warning(f'PythonREPL.run executed with code: {code}')
        logging_code.logger.error(f'PythonREPL.run executed with result: {result}')
        return result