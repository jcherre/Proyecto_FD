import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authentication via IAM
def nlu(comment):
    authenticator = IAMAuthenticator('71hpvrJO9Cji3KulSYAnfZffqTXeHDhKyiP9_sYonPoP')
    service = NaturalLanguageUnderstandingV1(
        version='2018-03-16',
        authenticator=authenticator)
    service.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/eef94920-06a4-4ccc-b709-caa1c34da1bf')

    response = service.analyze(
        text=comment,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
                                    limit=2))).get_result()
    # print(json.dumps(response,indent=2))
    return response

