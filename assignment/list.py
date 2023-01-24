clients = []

new_clients = ""
while new_clients != "quit":
    new_clients = input("What is the name of a new client?")
    clients.append(new_clients)

for client in clients:
    print(client)     