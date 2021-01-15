from django.urls import path


from memes import views

urlpatterns = [
    path("", views.MemesView.as_view(), name="memes"),
]