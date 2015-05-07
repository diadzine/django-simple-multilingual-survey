from django.db import models
from django.utils import timezone
from hvad.models import TranslatableModel, TranslatedFields
from django.utils.translation import ugettext_lazy as _
from multilingual_survey.managers import (
    SurveyManager, QuestionManager, ChoiceManager
)


class Survey(TranslatableModel):
    slug = models.SlugField(_('Survey slug'), max_length=200)
    hit = models.PositiveIntegerField(default=0)

    objects = SurveyManager()

    translations = TranslatedFields(
        title=models.CharField(_('Survey title'), max_length=200)
    )

    def __unicode__(self):
        title = self.lazy_translation_getter('title', None)
        if not title:
            title = getattr(self, 'slug', str(self.pk))
        return title

    def admin_title(self):
        return self.__unicode__()

    def questions(self):
        if self.pk:
            return self.question_set.language('').all()
        else:
            return None

    class Meta:
        ordering = ['pk']
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")


class Question(TranslatableModel):
    survey = models.ForeignKey(Survey)
    slug = models.SlugField(_('Question slug'), max_length=200)

    objects = QuestionManager()

    translations = TranslatedFields(
        question_text=models.CharField(_('Question text'), max_length=200)
    )

    def __unicode__(self):
        title = self.lazy_translation_getter('question_text', None)
        if not title:
            title = getattr(self, 'slug', str(self.pk))
        return title

    def admin_title(self):
        return self.__unicode__()

    def choices(self):
        if self.pk:
            return self.choice_set.language('').all()
        else:
            return None

    class Meta:
        ordering = ['pk']
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")


class Choice(TranslatableModel):
    question = models.ForeignKey(Question)

    objects = ChoiceManager()

    translations = TranslatedFields(
        choice_text=models.CharField(_('Choice text'), max_length=200)
    )

    def __unicode__(self):
        return self.lazy_translation_getter('choice_text', str(self.pk))

    def admin_title(self):
        return self.__unicode__()

    def get_survey(self):
        return self.question.survey

    class Meta:
        ordering = ['pk']
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")


class Response(models.Model):
    survey = models.ForeignKey(Survey)
    date_vote = models.DateTimeField(default=timezone.now)
    response_user = models.CharField(
        _('Name of user or identifier'),
        max_length=400
    )
    comments = models.TextField(
        _('Comments'),
        blank=True,
        null=True
    )
    ip = models.GenericIPAddressField()
    response_uuid = models.CharField(
        _("Response unique identifier"),
        max_length=36
    )

    def __unicode__(self):
        return ("response %s" % self.response_uuid)

    class Meta:
        ordering = ['-date_vote']
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")


class Answer(models.Model):
    response = models.ForeignKey(Response)
    choice = models.ForeignKey(Choice)

    class Meta:
        ordering = ['pk']
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
