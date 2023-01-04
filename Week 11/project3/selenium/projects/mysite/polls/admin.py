# Register your models here.
from django.contrib import admin

from .models import Choice, Question

from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import Group, User
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())

        
class ChoiceInline(admin.TabularInline):
      model = Choice
      extra = 3


class QuestionAdmin(admin.ModelAdmin):
      fieldsets = [(None,{'fields': ['question_text']}),('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),]
      inlines = [ChoiceInline]
      list_display = ('question_text', 'pub_date', 'was_published_recently')
      list_filter = ['pub_date']
      search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)

