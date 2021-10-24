from django.contrib import admin
from .models import Trivia

# Register your models here.
@admin.register(Trivia)
class TriviaModelAdmin(admin.ModelAdmin):
	list_display=['name','first_answer','second_answer','date_created']