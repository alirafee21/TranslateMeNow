from email.mime import audio
from urllib import response
from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
# Speech to Text
recognized_text = 'hello this is Python'
URL = {}
API_KEY = {}
authenticator = IAMAuthenticator(API_KEY)
s2t = SpeechToTextV1(
    authenticator=authenticator
)
s2t.set_service_url(URL)

filename = 'human.wav'
with open(filename, mode="rb") as wav:
    response=s2t.recognize(audio=wav, content_type='audio/wav')
    recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
    print(recognized_text)
url_it = {}
apikey_lt = {}

# Translation
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url_it)
# 
translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
translation =translation_response.get_result()
print(translation)