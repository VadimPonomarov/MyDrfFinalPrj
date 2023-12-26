import dataclasses


@dataclasses.dataclass
class J4fContentGenerator:
    init: str = None
    body: str = None
    task: str = None
    extras: str = None

    def __str__(self):
        return ' '.join(
            [
                str(v).strip() + '.'
                if v else ''
                for i, v
                in self.__dict__.items()
            ]
        )

    def __repr__(self):
        return self.__str__()
