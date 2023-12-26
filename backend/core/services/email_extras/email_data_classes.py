import dataclasses
from typing import Type

from attr import field
from django.template import Template


@dataclasses.dataclass
class SendEmailArgs:
    subject: str
    to: [str]
    context: dict
    template: Type[Template]
    from_email: str
    generated_content: Type[Template] = field(init=False)

    def __post_init__(self):
        self.generated_content = self.template.render(self.context)
