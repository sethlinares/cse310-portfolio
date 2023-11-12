import socket
import threading

def receive_message(client_socket): # function to receive messages from the server
    while True: # Loop to keep receiving messages until an error occurs
        try:
            message = client_socket.recv(1024).decode('utf-8') # Receive message from the server
            print(message) # Print the message from the other client
        except:
            print("An error occurred. Disconnecting from the server.")
            client_socket.close() # Close the socket
            break

def send_message(client_socket): # function to send messages to the server
    while True: 
        message = input("") # Take input from the user
        try:
            if message:
                client_socket.send(message.encode('utf-8')) # Send the message to the server
                print(f"You: {message}") # Print the message you sent
        except:
            print("An error occurred. Unable to send the message.")
            break

def main(): # main function
    HOST = '127.0.0.1' # The server's hostname / IP address which is localhost in this case
    PORT = 65432 # The port used by the server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object for the client
    client.connect((HOST, PORT)) # Connect to the server

    print("Connected to the chat server. Start typing to send messages.")
    
    receive_thread = threading.Thread(target=receive_message, args=(client,)) # Create a thread to receive messages
    receive_thread.start() # Start the thread for receiving messages

    send_thread = threading.Thread(target=send_message, args=(client,)) # Create a thread to send messages
    send_thread.start() # Start the thread for sending messages

if __name__ == "__main__":
    main()


# C:/Users/sethl/AppData/Local/Programs/Python/Python311/python.exe c:/Users/sethl/Documents/GitHub/cse310-portfolio/Chat_Application/chat_client.py