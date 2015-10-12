# coding: utf-8
def user(request):
    if hasattr(request, 'user'):
        return {'request':request }
    return {}
