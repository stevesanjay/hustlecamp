# Custom Exception with Error Code:

class ConnectionError(Exception):
    def __init__(self, error_code):
        self.error_code = error_code

def connect_to_server():
    server_status = False
    if not server_status:
        raise ConnectionError(404)
    else:
        print("Connected to server.")

try:
    connect_to_server()
except ConnectionError as e:
    print("Connection Error:", e.error_code)