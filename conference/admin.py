from django.contrib import admin
from .models import AbstractPaper, Conference

# Register your models here.
admin.site.register(Conference)
admin.site.register(AbstractPaper)
