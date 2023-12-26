import json
import asyncio

from django.http import HttpResponse
from rest_framework import status

from my_apps.adds.g4f_cfg import generate_task
from core.services.g4f_service import g4f_service


class DataBadWordsValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/api/adds' and request.method in ["POST", "PUT", "PATCH"]:
            if ('application/json' in request.META['CONTENT_TYPE']
                    and request.body):
                data = json.loads(request.body)
                task_title = generate_task(data['title'])
                title = asyncio.run(g4f_service(task_title))
                task_description = generate_task(data['description'])
                description = asyncio.run(g4f_service(task_description))
                data['title'] = title
                data['description'] = description
                json_data = json.dumps(data)
                request._body = json_data.encode()
                print(json_data)
            else:
                return HttpResponse("!!! 'CONTENT_TYPE' required is 'application/json'", status.HTTP_400_BAD_REQUEST)

        response = self.get_response(request)
        return response
