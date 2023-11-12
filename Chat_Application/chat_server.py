import socket
import threading

client_count = 0  # New variable to keep track of the number of connected clients

def handle_client(client_socket, client_id, clients): # Function to handle each client connection
    global client_count # Access the global variable
    while True: # Loop to keep receiving messages until an error occurs
        try:
            message = client_socket.recv(1024).decode('utf-8') # Receive message from the client
            if message:
                formatted_message = f"Client {client_id}: {message}" # Format the message with the client ID
                print(formatted_message)
                broadcast(formatted_message, client_socket, clients) # Broadcast the message to all clients
            else:
                break
        except:
            break
    client_socket.close() # Close the socket when the client disconnects
    clients.remove(client_socket) # Remove the client from the list of clients
    client_count -= 1  # Decrement client count when a client disconnects

def broadcast(message, sender_socket, clients): # Function to broadcast messages to all clients
    for client in clients: # Loop through all the clients
        if client is not sender_socket: # Send the message to all clients except the sender
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def receive_connections(server, clients): # Function to receive connections from new clients
    global client_count # Access the global variable
    while True:
        client, address = server.accept() # Accept new connection
        client_id = client_count # Assign client ID to the new client
        client_count += 1  # Increase client count for each new connection
        print(f"Client {client_id} connected with {str(address)}") # Print the address of the new client
        clients.add(client) # Add the new client to the list of clients
        thread = threading.Thread(target=handle_client, args=(client, client_id, clients)) # Create a thread to handle the new client
        thread.start() # Start the thread

def main():
    HOST = '127.0.0.1' # The server's hostname / IP address which is localhost in this case
    PORT = 65432 # The port used by the server

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object for the server
    server.bind((HOST, PORT)) # Bind the socket to the port
    server.listen() # Listen for connections

    clients = set() # Create a set to store the clients

    print("Server is listening...") # Print a message to indicate that the server is running
    receive_connections(server, clients) # Call the function to receive connections

if __name__ == "__main__":
    main()
