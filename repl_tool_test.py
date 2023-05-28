from PythonCodeRunner import PythonCodeRunner

import os
import tempfile
import random
import logging_code

from quart import request, Response

from base_tool import BaseTool
from python_repl import PythonREPL
from python_repl_tool import PythonREPLTool


class PythonREPLToolTest:
    def execute():
        code = "print('hello world')"
        print( "instantiating PythonREPLTool... " )
        tool = PythonREPLTool()
        print ( "calling tool._run... " )
        result = tool._run(code)
        logging_code.logger.warning(f'run_python_code executed with code: {code}')
        logging_code.logger.error(f'run_python_code executed with result: {result}')
        print ( "result: " + result )
        return result

if __name__ == "__main__":
    result = PythonREPLToolTest.execute()
    