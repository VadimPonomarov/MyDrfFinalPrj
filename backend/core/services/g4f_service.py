import json
import re
import g4f


async def g4f_service(content: str):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[
            {
                "role": "user",
                "content": f"{content}"
            }
        ],
    )
    regex = r"\{[^{}]*\}"

    matches = re.findall(regex, response)

    try:
        obj = json.loads(matches[0])
        return (obj.get('res'))
    except:
        print("Invalid JSON object")
