from modeltranslation.translator import translator, TranslationOptions
from .models import ClientFeedback

class ClientFeedbackTranslationOptions(TranslationOptions):
    fields = ['comment', 'position', 'company_name']

translator.register(ClientFeedback, ClientFeedbackTranslationOptions)
