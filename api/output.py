from json import dumps
from typing import Any, Dict, List


class Output:

    def __init__(self):
        pass

    def failure(self, message: str) -> (Dict[str, Any], str):
        res = {
            'status': 0,
            'message': message,
        }
        return self._compile(res)

    def success(
            self,
            data: List[Any],
            parameters: Dict[str, Any]
    ) -> (Dict[str, Any], str):
        res = {
            'status': 1,
            'record_count': len(data),
            'params': parameters,
            'data': data,
        }
        return self._compile(res)

    @staticmethod
    def _compile(res: Dict[str, Any], res_type='json') -> (str, str):
        if res_type != 'json':
            raise ValueError('Invalid res_type specified')
        response = dumps(res)
        content_type = 'application/json'
        return response, content_type
