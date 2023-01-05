from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import file
from PIL import Image
from PIL.ExifTags import TAGS
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import mail


def home(request):
    return render(request, "home.html")


def upload(request):
    x = request.FILES["file"]

    f = file(upload_to=x)
    f.save()

    return render(request, "home.html")


def show(request):
    # print(request.FILES["file"])

    connection = mail.get_connection()
    # Manually open the connection
    connection.open()

    # Construct an email message that uses the connection
    email1 = mail.EmailMessage(
        'Hello',
        'You tried to view uploaded files',
        'akhterrehan983@gmail.com',
        ['akhterrehan983@gmail.com'],
        connection=connection,
    )
    email1.send() # Se
    connection.close()

    username = request.POST.get("username")
    password = request.POST.get("pwd")
    print(username, password)
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        files = file.objects.all()
    else:
        files = []
        return HttpResponseRedirect("/home")
    # print(files)
    # print(files[0], type(files[0]))
    # ret = {}

    # image = Image.open(
    #     "D:/python test/upload_books/upload_books/media/WhatsApp_Image_2021-12-09_at_6.49.06_PM_BBWntqT.jpeg"
    # )
    # print(image)
    # # extracting the exif metadata
    # exifdata = image.getexif()

    # # looping through all the tags present in exifdata
    # print(exifdata)
    # for tagid in exifdata:

    #     # getting the tag name instead of tag id
    #     tagname = TAGS.get(tagid, tagid)

    #     # passing the tagid to get its respective value
    #     value = exifdata.get(tagid)

    #     # printing the final result
    #     print(f"{tagname:25}: {value}")
    return render(request, "home.html", {"files": files})
