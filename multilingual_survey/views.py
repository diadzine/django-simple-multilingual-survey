from django.shortcuts import get_object_or_404, redirect, render
from multilingual_survey.models import Survey
from multilingual_survey.forms import ResponseForm


def survey_form(request, slug):
    survey = get_object_or_404(Survey, slug=slug)
    form = ResponseForm(request=request, survey=survey)
    if request.method == 'POST':
        form = ResponseForm(data=request.POST, request=request, survey=survey)

        if form.is_valid():
            response = form.save()
            return redirect('survey:success', uuid=response.response_uuid)
        else:
            return render(
                request,
                'multilingual_survey/form.html',
                {'response_form': form, 'survey': survey}
            )
    else:
        return render(
            request,
            'multilingual_survey/form.html',
            {'response_form': form, 'survey': survey}
        )


def survey_success(request, uuid):
    return render(
        request,
        'multilingual_survey/success.html',
        {'uuid': uuid}
    )
