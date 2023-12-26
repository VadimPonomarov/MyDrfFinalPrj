from enum import Enum


class UserRoleEnum(Enum):
    BUYER = 'BUYER'
    SELLER = 'SELLER'

    def __init__(self, role: str):
        self.role = role

    @classmethod
    def get_choices(cls):
        return [(i.name, i.value) for i in cls]


class AccountTypeEnum(Enum):
    BASE = 'BASE'
    PREMIUM = 'PREMIUM'

    def __init__(self, acc_type: str):
        self.acc_type = acc_type

    @classmethod
    def get_choices(cls):
        return [(i.name, i.value) for i in cls]


class UserRegEx(Enum):
    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{6,}$',
        'Check if the password has a minimum of 6 characters, at least 1 uppercase letter, 1 lowercase letter, '
        'and 1 number with no spaces.'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.msg = msg
        self.pattern = pattern
