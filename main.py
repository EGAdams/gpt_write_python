import os
import subprocess
import tempfile
import random

from quart import request, Response
import quart_cors
import quart
# from code_runner import CodeRunner  # assuming the class is in a file named code_runner.py

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

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
