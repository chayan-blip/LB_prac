import socket
import random
class LoadBalancer:
    
    def __init__(self, serverpool=None):
        # Create a new socket which will listen to connections coming from clients.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 1000
        self.hostname = "127.0.0.1"
        self.add_server()
        self.serverpool = serverpool

    def start(self, ServerPool):
        # Bind the socket to the port and hostname specified in the init function
        self.socket.bind(self.hostname, self.port)
        # Start listening for incoming connections from clients
        self.socket.listen(5)
        # Accept a connection from a client
        conn, addr = self.socket.accept()
        # Send a message to the client
        conn.send("Welcome ... we will serve you in a minute")

    def run(self):
        while True:
            self.start()
            # Receive a message from the client
            data = self.conn.recv(1024)
            print(data)
            #if the client has timed out then close the connection
            if not data:
                break
            # # Send a response to the client
            # self.conn.send(data)
            # Close the connection with the client
            self.conn.close()


class LoadBalancingStrategy:
    def select_server(self,serverpool,request):
        pass


class RoundRobinStrategy(LoadBalancingStrategy):
    def __init__(self) -> None:
        self.server_index = 0

    def select_server(self,serverpool):
        server_to_return = serverpool.server_list[self.server_index]
        self.server_index = (self.server_index + 1) % len(serverpool.server_list)
        return server_to_return


class ServerPool:

    def __init__(self, strategy):
        self.server_list = []
        # Initialize the server pool selection strategy which returns
        # a specified server from the list of servers
        self.strategy = strategy
    
    def add_server(self, server):
        self.server_list.append(server)

    def remove_server(self, server, HealthCheck):
        # Remove the server from the pool if it is not working
        for server in self.server_list:
            if HealthCheck.is_down(server):
                self.server_pool.remove(server)

class HealthChecker:
    
    def __init__(self,server_pool) -> None:
        self.server_pool = server_pool
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data_packet = b'This is a test data packet'

    def is_down(self, server):
        # Check if the server is down
        try:
            # Connect to the server's host and port names as provided
            self.socket.connect(server.hostname, server.port)
            # Send a dummy packet to the server
            self.socket.send(self.data_packet)
            response = self.socket.recv(1024)
            if response.__contains__("200"):
            ## pretty bad way to check if the server is down
            ##trying to check if ok is returned in the payload somewhere has 200
                return True
            else:
                return False
        except:
            return True

        
class Port:
    pass

class Listner:
    pass

class Server:
    def __init__(self) -> None:
        self

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
    lb = LoadBalancer()
    lb.start()

if __name__ == "__main__":
    main()