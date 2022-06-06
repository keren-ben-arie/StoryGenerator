from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.forms import forms
from django.http import HttpResponse
from django.views.generic import TemplateView
from ModelCreation import gpt_3
from StoryTeller.logic.image_to_text import get_words_from_image
from django.shortcuts import redirect, render
from django.contrib.messages import INFO


class OnlineSamplerView(PermissionRequiredMixin, TemplateView):
    template_name = "index.html"
    permission_required = []
    story = None

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return view

    def get_title(self):
        return "A Picture is worth a thousand words."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["story"] = self.get_story()
        return context

    def post(self, request, *args, **kwargs):
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        words, path = get_words_from_image(file_url)
        self.story = gpt_3.generate_story(words)
        self.set_story(self.story)
        return redirect(self.request.path+"#second", {"story": self.story})

    def get_story(self):
      storage = getattr(self.request, '_messages', [])
      if not storage:
        return None
      message = [message for message in storage][-1].message

      return message


    def set_story(self, story, level=INFO):
        messages = self.request._messages
        messages.add(level, story)
