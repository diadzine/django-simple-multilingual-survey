==========================
Simple Multilingual Survey
==========================

Simple Multilingual Survey is a simple Django app to conduct Web-based survey.
For each survey and question, visitors can choose between a fixed number of choices.

Quick start
-----------

1. Add "multilingual_survey" to your INSTALLED_APPS settings like this:

    INSTALLED_APPS = (
        ...
        'multilingual_survey',
    )

2. Include the multilingual survey URLconf in your project urls.py like this::

    url(r'^survey/', include('multilingual_survey.urls', namespace='survey')),

3. Run `python manage.py migrate` to create the survey models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a survey, questions and choices (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/survey/slug-of-the-suvey/ to answer the survey.
