from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationUpperBond(LimitOffsetPagination):
    max_limit = 8