import os
import tempfile
import random
import logging_code

from quart import request, Response

from base_tool import BaseTool
from python_repl import PythonREPL
from python_repl_tool import PythonREPLTool


class PythonCodeRunner:
    @staticmethod
    async def run_python_code():
        print( "inside PythonCodeRunner.run_python_code... " )
        request_data = await request.get_json(force=True)
        code = request_data.get("code")
        print( "instantiating PythonREPLTool... " )
        tool = PythonREPLTool()
        print ( "calling tool._run... " )
        result = tool._run(code)
        logging_code.logger.warning(f'run_python_code executed with code: {code}')
        logging_code.logger.error(f'run_python_code executed with result: {result}')
        print ( "returning Response... " )
        return Response(response=result, status=200)