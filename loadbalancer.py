import socket
import random
class LoadBalancer:
    
    def __init__(self):
        # Create a new socket which will listen to connections coming from clients.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 1000
        self.hostname = 127.0.0.1

    def start(self):
        # Bind the socket to the port and hostname specified in the init function
        self.socket.bind(self.hostname, self.port)
        # Start listening for incoming connections from clients
        self.socket.listen(5)
        # Accept a connection from a client
        conn, addr = self.socket.accept()
        # Send a message to the client
        conn.send("Welcome ... we will serve you in a minute")
        


class Port:
    pass

class Listner:
    pass

class Server:
    pass

class Client:
    pass

# TODO: Implement dynamic versus static load balancing where the number of servers being load
    # balanced changes on the fly
# TODO: Implement failed requests
# TODO: Implement timeouts
# TODO: Implement cli
# TODO: Implement logging
# TODO: Implement different schemes for severs going online offline
# TODO: Implement different clients connections hogging the loadbalancers
# TODO: Implement if a client is selected and the loadbalancer is servicing
    # a request, then the loadbalancer when connection timeout happens automatically 
    # switches to another server.
# TODO: Implement different algorithms such as leaky bucket byte byte go
# TODO: Implement tests
class Monitor:
    # Is a process which continuously checks how many http transactions
    # are sent to the LoadBalancer, in a given 
    # 
    pass


class HttpTransaction:
    pass

def main():
    LoadBalancer = LoadBalancer()
    LoadBalancer.start()

if __name__ == "__main__":
    main()