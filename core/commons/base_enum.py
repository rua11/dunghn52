from enum import Enum


class StatusTypes(Enum):
    r"""
        - Trạng thái của tất cả các bảng
        - ACTIVE='Kích hoạt'
        - INACTIVE='Khóa'        
    """
    ACTIVE='Kích hoạt'
    INACTIVE='Khóa'

class SexType(Enum):
    MALE = 'Nam giới'
    FEMALE = 'Nữ giới'
    