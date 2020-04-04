

def request_handler(json_request):
    name = json_request["name"]
    age = json_request["age"]
    return {
        "message": "Hello " + name + "! You are " + str(age) + " years old."
    }


def handle_request(json):
    print(json["name"])
    return {
        "message": "hello123"
    }