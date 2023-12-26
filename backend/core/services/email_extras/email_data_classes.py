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

    def __call__(self, *args, **kwargs):
        return dict(from_email=self.from_email, to=self.to, subject=self.subject,
                    generated_content=self.generated_content)
