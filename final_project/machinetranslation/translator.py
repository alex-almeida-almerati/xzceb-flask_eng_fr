""" Provides functions for translating between english and french """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

""" Creates an instance of the IBM Watson Language translator """
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Uses IBM Watson™ Language Translator API from IBM Cloud platform 
    to translate english_text and returns french_text
    """
    result = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = result["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """
    Uses IBM Watson™ Language Translator API from IBM Cloud platform 
    to translate french_text and returns english_text
    """
    result = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = result["translations"][0]["translation"]
    return english_text
