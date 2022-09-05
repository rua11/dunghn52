import grpc
from rpc.generated import teacher_pb2, teacher_pb2_grpc

# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = teacher_pb2_grpc.TeacherControllerStub(channel)
#     print("client dang chay")
#     res= stub.TeacherById(teacher_pb2.TeacherByIdRequest(id="2b8281c9-caf3-43c7-86c5-843146e91c7d"))
#     print(res)


print("1")
with open('rpc/certs/cert.pem', 'rb') as f:
    creds = grpc.ssl_channel_credentials(f.read())
print("2")
channel = grpc.secure_channel('localhost:50051', creds)
print("3")
stub = teacher_pb2_grpc.TeacherControllerStub(channel)


print("Chi tiết SP1")
response = stub.TeacherById(teacher_pb2.TeacherByIdRequest(id = "2b8281c9-caf3-43c7-86c5-843146e91c7d"))
print("4")
print(response)
print("Chi tiết Danh mục")

