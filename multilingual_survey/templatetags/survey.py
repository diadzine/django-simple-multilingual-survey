from classytags.arguments import StringArgument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template
from django.conf import settings
from multilingual_survey.forms import ResponseForm
from multilingual_survey.models import (
    Survey, Question, Choice
)

register = template.Library()


class ShowSurvey(InclusionTag):
    """
    render a survey
    - slug: slug of the survey to render
    - lang: language used to render the survey
    - template: template used to render the survey
    """
    name = 'show_survey'
    template = 'multilingual_survey/survey.html'

    options = Options(
        StringArgument('slug', required=True),
        StringArgument('lang', default=settings.LANGUAGE_CODE, required=False),
        StringArgument('template', default='menu/menu.html', required=False),
    )

    def get_context(self, context, slug, lang, template):
        try:
            # If there's an exception (500),
            # default context_processors may not be called.
            request = context['request']
        except KeyError:
            return {'template': 'multilingual_survey/empty.html'}

        # FIXME
        # Get survey data
        try:
            survey = Survey.objects.get(slug=slug)
            form = ResponseForm(request=request, survey=survey)

        except Survey.DoesNotExist:
            return {'error': 'Survey does not exist'}

        try:
            context.update({
                'response_form': form,
                'survey': survey,
                'template': template,
            })
        except:
            context = {"template": template}
        return context


register.tag(ShowSurvey)
