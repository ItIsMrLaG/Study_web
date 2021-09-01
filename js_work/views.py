from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.

def param_reader (request):
    info = request.GET.get('value')
    id = request.GET.get('id')
    buf = {"value": info, "id": id}
    print(buf)
    return render(request, 'js_work/test_js.html')

def json_sender(request):
    result = {"info": "from", "bd": "json"}
    return HttpResponse(json.dumps(result), content_type='myJson')
