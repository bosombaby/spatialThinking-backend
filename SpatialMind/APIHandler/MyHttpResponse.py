import json
import this

from django.http import HttpResponse, JsonResponse


class MyAPIResponse:
    def __init__(self, status=200, msg='success', data=None, success=True):
        if data is None:
            data = []
        self.status = status
        self.msg = msg
        self.data = data
        self.success = success

    # 后续可以扩展封装，目前架子是这样
    def to_json(self):
        # 将HTTP响应的各种维度转换为JSON格式
        data = json.dumps({
            'status': self.status,
            'msg': self.msg,
            'data': self.data,
            'success': self.success
        }, ensure_ascii=False, indent=4)

        response = HttpResponse(data)
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Origin'] = '*'
        print('response', response)
        return response


def test_api():
    response = MyAPIResponse(200, 'success'[{'status': 'hhhh哈哈哈哈', 'msg': 'success'}])
    print('Response', response.to_json())


if __name__ == '__main__':
    test_api()
