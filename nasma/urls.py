from django.urls import path, include

urlpatterns = [
    path("article/", include("article.urls")),
    path("breathing/", include("breathing.urls")),
    path("pss/", include("pss.urls")),
]