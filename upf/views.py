import os

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'upf/index.html')


def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        # 打开特定的文件进行二进制的写操作
        destination = open(os.path.join(
            "C:\\Django\\upload", myFile.name), 'wb+')
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
