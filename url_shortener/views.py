from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hashlib import md5
from .models import URLRecord


# Create your views here.
def index(request):
    template_name = "url_shortener/index.html"
    data = request.POST.get("data")

    return render(request, template_name)


@api_view(["GET", "POST"])
def shorten_url(request):

    if request.method == "POST":
        long_url = request.data.get("url")
        print(long_url)
        id = md5(long_url.encode("utf-8")).hexdigest()[0:7]
        short_url = f"http://127.0.0.1:8000/tiny/{id}/"
        print(short_url)
        url = URLRecord.objects.filter(id=id).first()
        if url:
            context = {"short_url": short_url}
            return Response(context, status=status.HTTP_200_OK)
        else:
            URLRecord.objects.create(id=id, long_url=long_url, short_url=short_url)
            context = {"short_url": short_url}
            return Response(context, status=status.HTTP_201_CREATED)

    if request.method == "GET":

        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "POST"])
def long_url(request, id):
    if request.method == "GET":
        url = URLRecord.objects.filter(id=id).first()
        return redirect(url.long_url)
