''' Imports packages'''
import socket
import openai
openai.api_key = "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"





# Create server socket
HOST = '127.0.0.1'
PORT = 8484

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    con, add = s.accept()

    with con:
        print("Conectado como ?", (add))

        while True:
            data = con.recv(1024)
            if not data:
                break

        con.sendall(data)

completion = openai.Completion.create(engine="text-davinci-003", prompt = data, max_tokens = 2048)
print(completion.choices[0].text)