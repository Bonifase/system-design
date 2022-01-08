from django.urls import path
from .views import index, shorten_url, long_url

urlpatterns = [
    # path("", index, name="home"),
    path("tiny/", shorten_url, name="shorten"),
    path("tiny/<str:id>/", long_url, name="long-url"),
]
