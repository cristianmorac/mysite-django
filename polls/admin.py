from django.contrib import admin
from .models import Question, Choice
# Register your models here.

''' Modificar formulario '''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # Dividir el formulario
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines =[ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
