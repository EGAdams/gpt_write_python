@app.post("/read_file")
async def read_file():
    request_data = await quart.request.get_json(force=True)
    filepath = request_data.get("filepath")

    if not filepath:
        return Response(response='No file path provided', status=400)

    if not os.path.exists(filepath):
        return Response(response='File does not exist', status=404)

    with open(filepath, 'r') as file:
        content = file.read()

    return Response(response=content, status=200)