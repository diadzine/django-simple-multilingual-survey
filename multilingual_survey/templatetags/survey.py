from classytags.arguments import StringArgument
from classytags.core import Options
from classytags.helpers import InclusionTag
from cms.utils.i18n import force_language, get_language_objects
from django import template


register = template.Library()


class ShowSurvey(InclusionTag):
    """
    render a survey
    - lang: language used to render the survey
    - template: template used to render the survey
    """
    name = 'show_survey'
    template = 'multilingual_survey/survey.html'

    options = Options(
        StringArgument('lang', default=0, required=False),
        StringArgument('template', default='menu/menu.html', required=False),
    )

    def get_context(self, context, lang, template):
        try:
            # If there's an exception (500),
            # default context_processors may not be called.
            request = context['request']
        except KeyError:
            return {'template': 'multilingual_survey/empty.html'}

        # FIXME
        # Get survey data

        try:
            context.update({
                # 'survey': survey_form,
                'template': template,
            })
        except:
            context = {"template": template}
        return context


register.tag(ShowMenu)
