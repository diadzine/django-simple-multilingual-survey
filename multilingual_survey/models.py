from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation


class SurveyTranslation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey('Survey', related_name='translations')
    title = models.CharField(max_length=200)


class Survey(MultilingualModel):
    slug = models.SlugField(max_length=200)
    hit = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.unicode_wrapper('title', default='Survey')

    def admin_title(self):
        return self.__unicode__()

    def questions(self):
      if self.pk:
          return Question.objects.filter(survey=self.pk)
      else:
          return None


class QuestionTranslation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey('Question', related_name='translations')
    question_text = models.CharField(max_length=200)


class Question(MultilingualModel):
    survey = models.ForeignKey(Survey)

    def __unicode__(self):
        return self.unicode_wrapper('question_text', default='Question')

    def admin_title(self):
        return self.__unicode__()

    def choices(self):
      if self.pk:
          return Choice.objects.filter(question=self.pk)
      else:
          return None


class ChoiceTranslation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')

    parent = models.ForeignKey('Choice', related_name='translations')
    choice_text = models.CharField(max_length=200)


class Choice(MultilingualModel):
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.unicode_wrapper('choice_text', default='Choice')

    def admin_title(self):
        return self.__unicode__()


class Response(models.Model):
    survey = models.ForeignKey(Survey)
    date_vote = models.DateTimeField(auto_now_add=True)
    response_user = models.CharField('Name of user', max_length=400)
    comments = models.TextField('Any additional Comments', blank=True, null=True)
    ip = models.IPAddressField()
    response_uuid = models.CharField("Response unique identifier", max_length=36)

    def __unicode__(self):
        return ("response %s" % self.response_uuid)


class Answer(models.Model):
    response = models.ForeignKey(Response)
    choice = models.ForeignKey(Choice)
