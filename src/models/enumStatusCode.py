from enum import Enum
class StatusCode(Enum):
    CONTUINUE = 100
    OK = 200
    MOVED = 301
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_ERROR = 502