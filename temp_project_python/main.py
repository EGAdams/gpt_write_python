import ast
import sys
from io import StringIO
from typing import Dict, Optional

from quart import request, Response, Quart
import quart_cors
import quart

from base_tool import BaseTool
from python_repl import PythonREPL
from python_repl_tool import PythonREPLTool
from python_ast_repl_tool import PythonAstREPLTool

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/run_python_code")
async def run_python_code():
    request_data = await quart.request.get_json(force=True)
    code = request_data.get("code")
    tool = PythonREPLTool()
    result = tool._run(code)
    return Response(response=result, status=200)

@app.post("/run_python_ast_code")
async def run_python_ast_code():
    request_data = await quart.request.get_json(force=True)
    code = request_data.get("code")
    tool = PythonAstREPLTool()
    result = tool._run(code)
    return Response(response=result, status=200)

# ... rest of the file ...
