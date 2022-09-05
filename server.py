import grpc
from concurrent import futures
from rpc.handlers.teacher_handler import grpc_teacher_handler

def serve():
    print("server grpc dang chay")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_teacher_handler(server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    print("server dang chay")

    # print("sap cahy")
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # with open('rpc/certs/key.pem', 'rb') as f:
    #     private_key = f.read()
    # with open('rpc/certs/cert.pem', 'rb') as f:
    #     certificate_chain = f.read()
    # server_credentials = grpc.ssl_server_credentials( ( (private_key, certificate_chain), ) )
    # # Adding GreeterServicer to server omitted
    # grpc_teacher_handler(server)
    # server.add_secure_port('[::]:50051', server_credentials)
    # server.start()
    # server.wait_for_termination()
    # print("dang chay")
    
# Server sleep omitted

if __name__ == '__main__':
    serve()

