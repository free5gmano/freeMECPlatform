def put_payload_parser(request):
    data = request.body.decode("utf-8")
    data = data.replace("-", "")
    data = data.replace("Content-Disposition: form-data; name=", "")
    data = data.replace("\r\n\r", "")
    data = data.replace("\n", "")
    data = data.split("\"")
    data.pop(0)
    payload = {}
    for i in range(0, len(data), 2):
        payload[data[i]] = data[i+1].split("\r")[0]
    return payload