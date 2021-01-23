from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api.views import AddView, DeleteView

app_name = 'api'

urlpatterns = [
    path('<int:pk>/add/', AddView.as_view(), name='add_friend'),
    path('<int:pk>/delete', DeleteView.as_view(), name='del_friend'),
]