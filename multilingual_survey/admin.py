from django.contrib import admin
from multilingual_model.admin import TranslationStackedInline
from multilingual_survey.models import (Survey, SurveyTranslation,
                                        Question, QuestionTranslation,
                                        Choice, ChoiceTranslation)


class SurveyTranslationInline(TranslationStackedInline):
    model = SurveyTranslation


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('admin_title',)
    inlines = [SurveyTranslationInline]


admin.site.register(Survey, SurveyAdmin)


class QuestionTranslationInline(TranslationStackedInline):
    model = QuestionTranslation


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('admin_title', 'survey',)
    ordering = ['id']
    inlines = [QuestionTranslationInline]


admin.site.register(Question, QuestionAdmin)


class ChoiceTranslationInline(TranslationStackedInline):
    model = ChoiceTranslation


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('admin_title', 'question',)
    ordering = ['id']
    inlines = [ChoiceTranslationInline]


admin.site.register(Choice, ChoiceAdmin)
