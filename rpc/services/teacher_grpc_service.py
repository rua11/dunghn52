from unicodedata import name
from core.commons.context import ExceptionResponse, SuccessResponse
from modules.users.schemas.teacher_schema import TeacherGrpcResponse
from modules.users.service.teacher_service import TeacherService
from rpc.generated import teacher_pb2, teacher_pb2_grpc
class TeacherGrpcService(teacher_pb2_grpc.TeacherControllerServicer):
    def TeacherById(self, request, context):
        try:
            teacher = TeacherService().filter_teacher_by_id(id = request.id)
            teacher = TeacherGrpcResponse(**teacher.__dict__)
            print(teacher.dict())
            res = SuccessResponse(data=teacher.dict())
            return teacher_pb2.TeacherResponse(**res.__dict__)
        except Exception as ex:
            res = ExceptionResponse(errors=str(ex.args))
            return teacher_pb2.TeacherResponse(**res.__dict__)