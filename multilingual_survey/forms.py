from django import forms
from django.forms import models
from django.utils.safestring import mark_safe
import uuid
from multilingual_survey.models import Response, Answer, Question, Choice


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class ResponseForm(models.ModelForm):
    class Meta:
        model = Response
        fields = ('comments',)

    def __init__(self, request=None, *args, **kwargs):
        survey = kwargs.pop('survey')
        self.survey = survey
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.response_uuid = random_uuid = uuid.uuid4().hex

        # Getting IP Address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        self.ip = ip


        data = kwargs.get('data')
        for q in survey.questions():
            question_choices = q.choices()
            self.fields["question_%d" % q.pk] = forms.ModelChoiceField(label=q.question_text,
                    queryset=question_choices, empty_label=None,
                    widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))

            self.fields["question_%d" % q.pk].required = True
            self.fields["question_%d" % q.pk].widget.attrs["class"] = "required"

            if data:
                self.fields["question_%d" % q.pk].initial = data.get('question_%d' % q.pk)

    def save(self, commit=True):
        # save the response object
        response = super(ResponseForm, self).save(commit=False)
        response.survey = self.survey
        response.ip = self.ip
        response.response_uuid = self.response_uuid
        response.save()

        # create an answer object for each question and associate it with this
        # response.
        for field_name, field_value in self.cleaned_data.iteritems():
            if field_name.startswith("question_"):
              a = Answer()
              a.choice = field_value
              a.response = response
              a.save()
        return response
