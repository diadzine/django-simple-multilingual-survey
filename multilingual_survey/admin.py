from django.contrib import admin
from hvad.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline
from multilingual_survey.models import (Survey, Question, Choice)


# class SurveyTranslationInline(TranslationStackedInline):
#     model = SurveyTranslation


# class SurveyAdmin(admin.ModelAdmin):
#     list_display = ('admin_title',)
#     inlines = [SurveyTranslationInline]


# admin.site.register(Survey, SurveyAdmin)


# class QuestionTranslationInline(TranslationStackedInline):
#     model = QuestionTranslation


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('admin_title', 'survey',)
#     ordering = ['id']
#     inlines = [QuestionTranslationInline]


# admin.site.register(Question, QuestionAdmin)


# class ChoiceTranslationInline(TranslationStackedInline):
#     model = ChoiceTranslation


# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('admin_title', 'question',)
#     ordering = ['id']
#     inlines = [ChoiceTranslationInline]


# admin.site.register(Choice, ChoiceAdmin)

class QuestionInline(TranslatableTabularInline):
    model = Question


class SurveyAdmin(TranslatableAdmin):
    list_display = ('admin_title',)
    inlines = [QuestionInline]


class ChoiceInline(TranslatableTabularInline):
    model = Choice


class QuestionAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'survey')
    inlines = [ChoiceInline]


class ChoiceAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'question', 'get_survey')


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
