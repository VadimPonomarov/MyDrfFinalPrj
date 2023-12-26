from enum import Enum


class CarMarkEnum(Enum):
    MARK = (
        r'^\w[\w\d]{1,19}$',
        'Name is a string of characters + digits'

    )
    MODEL = (
        r'^\w[\w\d]{1,19}$',
        'Name is a string of characters + digits'

    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.msg = msg
        self.pattern = pattern


class CurrenciesEnum(Enum):
    UAH = 'UAH'
    USD = 'USD'
    EUR = 'EUR'

    def __init__(self, cur: str):
        self.cur = cur

    @classmethod
    def get_choices(cls):
        return [(i.name, i.value) for i in cls]
