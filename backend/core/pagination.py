import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100


class CustomPagination(ResultsSetPagination):
    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count / self.get_page_size(self.request))
        current_page = self.page.number
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            '-------------------': '',
            '# page': current_page,
            '# out of PAGES': total_pages,
            '# TOTAL items': count,
            '===================': '',
            'results': data
        })
