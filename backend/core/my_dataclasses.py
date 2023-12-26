import dataclasses

from core.enums import user_enums


@dataclasses.dataclass
class UserAccountDataClass:
    id: int
    client_type: user_enums.UserRoleEnum
    account_type: user_enums.AccountTypeEnum


@dataclasses.dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    account: UserAccountDataClass
