from django.db import models
from django.utils import timezone
from hvad.models import TranslatableModel, TranslatedFields


class Survey(TranslatableModel):
    slug = models.SlugField(max_length=200)
    hit = models.PositiveIntegerField(default=0)

    translations = TranslatedFields(
        title=models.CharField(max_length=200)
    )

    def __unicode__(self):
        return self.safe_translation_getter('title', str(self.pk))

    def admin_title(self):
        return self.__unicode__()

    def questions(self):
        if self.pk:
            return self.question_set.all()
        else:
            return None


class Question(TranslatableModel):
    survey = models.ForeignKey(Survey)
    slug = models.SlugField(max_length=200)

    translations = TranslatedFields(
        question_text=models.CharField(max_length=200)
    )

    def __unicode__(self):
        return self.safe_translation_getter('question_text', str(self.pk))

    def admin_title(self):
        return self.__unicode__()

    def choices(self):
        if self.pk:
            return self.choice_set.all()
        else:
            return None


class Choice(TranslatableModel):
    question = models.ForeignKey(Question)

    translations = TranslatedFields(
        choice_text=models.CharField(max_length=200)
    )

    def __unicode__(self):
        return self.safe_translation_getter('choice_text', str(self.pk))

    def admin_title(self):
        return self.__unicode__()


class Response(models.Model):
    survey = models.ForeignKey(Survey)
    date_vote = models.DateTimeField(default=timezone.now)
    response_user = models.CharField('Name of user', max_length=400)
    comments = models.TextField(
        'Any additional Comments',
        blank=True,
        null=True
    )
    ip = models.GenericIPAddressField()
    response_uuid = models.CharField(
        "Response unique identifier",
        max_length=36
    )

    def __unicode__(self):
        return ("response %s" % self.response_uuid)


class Answer(models.Model):
    response = models.ForeignKey(Response)
    choice = models.ForeignKey(Choice)
