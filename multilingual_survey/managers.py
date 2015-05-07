from hvad.models import TranslationManager


class SurveyManager(TranslationManager):
    def get_queryset(self, *args, **kwargs):
        return super(SurveyManager, self)\
            .get_queryset(*args, **kwargs)\
            .using(self._db)


class QuestionManager(TranslationManager):
    def get_queryset(self, *args, **kwargs):
        return super(QuestionManager, self)\
            .get_queryset(*args, **kwargs)\
            .using(self._db)


class ChoiceManager(TranslationManager):
    def get_queryset(self, *args, **kwargs):
        return super(ChoiceManager, self)\
            .get_queryset(*args, **kwargs)\
            .using(self._db)
