from django.urls import path, include

from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dialogs/', DialogsView.as_view(), name='dialogs'),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('<int:pk>/create/', CreateDialogView.as_view(), name='create_dialog'),
]