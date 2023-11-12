# Overview

This chat application, written in Python, provides a simple but intuitive interface to communicate with other users. Users can interact with a console application to send and receive messages from other users. The program utilizes fundamental aspects of Python, such as sockets, threads, and other structures. This software serves as a practical application of core programming concepts and is a great example of how Python can be used to create a useful program especially in the field of networking. Overall, this project was a great learning experience and I am excited to continue learning Python and other key concepts like networking.

To use the chat application, the server must be running first. Once the server is running, clients can connect to the server and start sending messages. The server will then broadcast the messages to all other connected clients. 

# Video Demonstration

[Chat Application Demo Video](https://youtu.be/H9hdKUqbYHY)

# Network Communication

The architecture that I used was client/server. The server is the host and the client is the guest. The server is the one that is listening for a connection from the client. Once the client connects to the server, the server will send a message to the client. The client will then send a message back to the server. The server will then send a message back to the client. The client will then send a message back to the server. This process will continue until the client sends a message to the server saying that it wants to disconnect. The server will then send a message back to the client saying that it is disconnecting. The client will then disconnect from the server.

- **Protocol Used:** TCP (Transmission Control Protocol)
- **Port Number:** The application uses port `65432` for the TCP connections.
- TCP is chosen for its reliability in data transmission, ensuring that messages are delivered in order and without loss, which is essential for a chat application.

Messages in this chat application are exchanged in plain text format and encoded in UTF-8.

- **From Client to Server:**
  - Clients send their messages as plain text strings to the server.
  - Example: A user types `"Hello World"` and it's sent as is to the server.

- **From Server to Clients:**
  - When the server receives a message from one of the clients, the server adds an identifier (like Client 1, Client 2, etc) to this message to indicate its origin and then broadcasts it to all other connected clients.
  - Example: If Client 1 sends `"Hello World"`, other clients receive `"Client 1: Hello World"`.

# Development Environment

* Visual Studio Code

* Programming Language: Python

* Libraries: `socket`, `threading`

# Useful Websites

* [Socket Documentation](https://docs.python.org/3/library/socket.html)
* [Threading Documentation](https://docs.python.org/3/library/threading.html)
* [Python Tutorial](https://www.w3schools.com/python/)

# Future Work

* Add a GUI for the application
* Allow for file transfer
* Add some encryption or security