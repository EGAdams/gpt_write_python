class CodeRunner:
    @staticmethod
    async def run_code():
        request_data = await quart.request.get_json(force=True)
        file_path = request_data.get("file_path")

        if not file_path or not os.path.isfile(file_path):
            return Response(response='Invalid file path', status=400)

        try:
            output = subprocess.check_output(["python", file_path], stderr=subprocess.STDOUT)
            return Response(response=output.decode(), status=200)
        except subprocess.CalledProcessError as e:
            return Response(response=e.output.decode(), status=400)