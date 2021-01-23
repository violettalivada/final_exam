from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from webapp.models import *
from webapp.forms import SimpleSearchForm, MessageForm


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'users'
    form_class = SimpleSearchForm
    paginate_by = 3
    paginate_orphans = 0

    def get_queryset(self):
        usr = get_user_model()
        data = usr.objects.all()
        if self.request.user.is_authenticated:
            data = usr.objects.exclude(pk=self.request.user.pk)
        return data


class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'dialogs.html', {'user_profile': request.user, 'chats': chats})


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(request, 'messages_list.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('webapp:messages', kwargs={'chat_id': chat_id}))

