from quart import Quart, request, jsonify
from code_writer import PythonFileExecutor

app = Quart(__name__)
executor = PythonFileExecutor()

@app.route('/execute_python_file', methods=['POST'])
async def execute_python_file():
    data = await request.get_json()
    filename = data.get('filename')
    result = executor.execute_python_file(filename)
    return jsonify(result)