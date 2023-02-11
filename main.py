# import packages
import socket, requests
import openai
openai.api_key = "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"

# Create server socket
HOST = '127.0.0.1'
PORT = 8484

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen
    

completion = openai.Completion.create(engine="text-davinci-003", prompt = "Genera un hello world en python", max_tokens = 2048)
print(completion.choices[0].text)




