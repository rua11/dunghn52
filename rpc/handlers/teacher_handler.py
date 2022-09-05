from rpc.generated import teacher_pb2_grpc
from rpc.services.teacher_grpc_service import TeacherGrpcService

def grpc_teacher_handler(server):
    teacher_pb2_grpc.add_TeacherControllerServicer_to_server(TeacherGrpcService(), server)