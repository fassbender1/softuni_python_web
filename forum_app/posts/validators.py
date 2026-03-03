from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# def bad_language_validator(value: str):
#     bad_words = {'fuck', 'shit', 'cunt'} # 'bad_word1', 'bad_word2'
#
#     if bad_words.intersection(value.split()):
#         raise ValidationError('This post contains bad language!')

@deconstructible
class BadLanguageValidator:
    def __init__(self, message: str) -> None:
        self.message = message

    def __call__(self, value: str) -> None:
        bad_words = {'fuck', 'shit', 'cunt'}

        if bad_words.intersection(value.split()):
            raise ValidationError('This text contains bad language!')