class LoadBalancer:
    
    def __init__(self,
                 port=None,
                 hostName=None):
        # Create a new address to which the connecting requesters will connect to.
        self.Load_balancer_address = 


class Port:
    pass

class Listner:
    pass

class Server:
    pass

class Client:
    pass

# TODO: Implement dynamic versus static load balancing where the number of servers being load
    # balanced changes. on th fly
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
    pass

if __name__ == "__main__":
    main()