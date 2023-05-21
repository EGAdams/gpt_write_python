# 
# Main Python file: main.py 

# Description:
# This file is the entry point for your plugin.

# It contains the following methods:
#   * execute_python_file - Accepts a filename and returns a JSON object.
#   * write_code - Accepts a code string and writes it to a file.
# 
# ``` python
import os
import subprocess
import tempfile
import random

from quart import request, Response, Quart, jsonify
import quart_cors
import quart
# from code_runner import CodeRunner  # assuming the class is in a file named code_runner.py


from base_tool import BaseTool
from python_repl import PythonREPL
from python_repl_tool import PythonREPLTool
from python_ast_repl_tool import PythonAstREPLTool

from python_file_executor import PythonFileExecutor

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

@app.post("/write_code")
async def write_code():
    request_data = await quart.request.get_json(force=True)
    code = request_data.get("code")
    directory = request_data.get("directory")
    filename = request_data.get("filename", "code.py")

    if not code:
        return Response(response='No code provided', status=400)

    if not directory:
        directory = os.path.join(tempfile.gettempdir(), str(random.randint(1000, 9999)))

    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, filename)

    with open(file_path, 'w') as file:
        file.write(code)

    return Response(response=f'Code written to {file_path}', status=200)

@app.post("/read_file")
async def read_file():
    request_data = await quart.request.get_json(force=True)
    filepath = request_data.get("filepath")

    if not filepath:
        return Response(response='No filepath provided', status=400)

    if not os.path.exists(filepath):
        return Response(response=f'File {filepath} does not exist', status=404)

    with open(filepath, 'r') as file:
        content = file.read()

    return Response(response=content, status=200)




# app = Quart(__name__)
# executor = PythonFileExecutor()

# @app.route('/execute_python_file', methods=['POST'])
# async def execute_python_file():
#     data = await request.get_json()
#     filename = data.get('filename')
#     result = executor.execute_python_file(filename)
#     return jsonify(result)

# @app.post("/run_code")
# async def run_code():
    # return await CodeRunner.run_code()

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
#```