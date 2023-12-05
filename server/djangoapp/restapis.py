import requests
import json
# import related models here
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions

credentials = {
    "IAM_API_KEY": "4iKJcQaT1ZJq6tbnwC4TZIqUwAoLz4UjLA7RBEm01OGN",
    "COUCH_URL": "https://3c366aa0-e65a-45df-b3a8-94d6d0482251-bluemix.cloudantnosqldb.appdomain.cloud"
}

#iam_token = "eyJraWQiOiIyMDIzMTEwNzA4MzYiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjYwMDNNS0lFIiwiaWQiOiJJQk1pZC02NjYwMDNNS0lFIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiZmNlYzFhY2UtNjFlMy00NzFmLTk2NTMtMjE2ODk1ZGUyMGI4IiwiaWRlbnRpZmllciI6IjY2NjAwM01LSUUiLCJnaXZlbl9uYW1lIjoiS3lsZSIsImZhbWlseV9uYW1lIjoiSHVtcGhyZXkiLCJuYW1lIjoiS3lsZSBIdW1waHJleSIsImVtYWlsIjoia3lsZXVuaXZlcnNpdGllc0BnbWFpbC5jb20iLCJzdWIiOiJreWxldW5pdmVyc2l0aWVzQGdtYWlsLmNvbSIsImF1dGhuIjp7InN1YiI6Imt5bGV1bml2ZXJzaXRpZXNAZ21haWwuY29tIiwiaWFtX2lkIjoiSUJNaWQtNjY2MDAzTUtJRSIsIm5hbWUiOiJLeWxlIEh1bXBocmV5IiwiZ2l2ZW5fbmFtZSI6Ikt5bGUiLCJmYW1pbHlfbmFtZSI6Ikh1bXBocmV5IiwiZW1haWwiOiJreWxldW5pdmVyc2l0aWVzQGdtYWlsLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJkZmU1NDFmMDMxZjA0YzhmYTU0OTU2ZjRlYWRmYmZjNiIsImltc191c2VyX2lkIjoiMTE1OTQ5NzYiLCJmcm96ZW4iOnRydWUsImltcyI6IjI3NjQxOTIifSwiaWF0IjoxNzAxNzYwNzM4LCJleHAiOjE3MDE3NjQzMzgsImlzcyI6Imh0dHBzOi8vaWFtLmNsb3VkLmlibS5jb20vaWRlbnRpdHkiLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.jx051qqfTB1sINhlBuVv2Z85rhv-P7raLRss_ggJegIXkEm7vOQt-mr3d036Xvj77odY7I8B1IBB-YR-c3KgLC7iTZQT-JX43quQGVlvY7k1lMuJxSOa_c_38x8xTXl6Hr_l8n2qkRl3QDjmsHA0hx0d9eGmhKObGqoEMS8RmbMqE0aGTvibLCLerYklp9ETMjkMmYXQW4sYUR0elWwYBzKqPDV9-_Ojmi2Ywx2y_FuY5Gyjch-dfCTnZvMLBSwRmJGjudkFG1DFMDzepWy1qnBFfeCDnRZZMyRgqQBOHh7WH7V9s2JFkTDfEDyNE5V_f0D793c2cZLixXyaAm0XHA"
#authorization = "Bearer " + iam_token

authenticator = IAMAuthenticator('8yslbBpV3Cvitwv3cWl_DXpImlQ8KohHCRfBekRjS8pU')
natural_language_understanding = NaturalLanguageUnderstandingV1( \
    version='2022-04-07', \
    authenticator=authenticator \
)
# Test

natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/2b0fa95e-f0aa-4d1c-beec-d8387c619dca')

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, json_payload, **kwargs):
    print(kwargs)
    print("POST to {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        token_url = 'https://iam.cloud.ibm.com/identity/token'
        iam_response = requests.post(token_url, headers={'Content-Type': 'application/x-www-form-urlencoded', 'accept': 'application/json'}, params=kwargs, data={ 'grant_type': 'urn:ibm:params:oauth:grant-type:apikey', 'apikey': 'TCzKPBR9r1tifaSWWPk88_H8yvzqhqxNMZ-8sW0JtfEV' })
        iam_response_data = json.loads(iam_response.text)
        print('IAM_RESPONSE')
        # Test
        print(iam_response_data)
        iam_token = iam_response_data["access_token"]
        authorization = "Bearer " + iam_token
        response = requests.post(url, headers={'Content-Type': 'application/json', 'authorization': authorization}, params=kwargs, json=json_payload)
        status_code = response.status_code
        print("With status {} ".format(status_code))
        json_data = json.loads(response.text)
        return json_data
    except:
        # If any error occurs
        print("Network exception occurred")
        return {}

# Cloud Function
def cloud_function(url, json_payload, **kwargs):
    cf_res = post_request(url, json_payload)
    print('CF_RESULT')
    print(cf_res)
    print('AFTER_CF_RES')
    return cf_res['response']['result']

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = cloud_function(url, credentials)
    print('JSON_RESULT: ')
    print(json_result)
    dealers = json_result["res"]
    # Test
    for dealer in dealers:
        dealer_doc = dealer
        results.append(CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], state=dealer_doc["state"], zip=dealer_doc["zip"]))
    return results



# Helper function
def get_apparent_value(obj, key, backup_value='None'):
    value = backup_value
    if key in obj:
        value = obj[key]
    return value


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_reviews_from_cf(url, dealer_id):
    results = []
    # Call get_request with a URL parameter
    payload = {
        "IAM_API_KEY": credentials["IAM_API_KEY"],
        "COUCH_URL": credentials["COUCH_URL"],
        "dealerId": dealer_id
    }
    json_result = cloud_function(url, credentials)
    print('JSON_RESULT: ')
    print(json_result)
    reviews = json_result["res"]
    # Test 11
    for review in reviews:
        review_doc = review
        print('REVIEW: ')
        print(review_doc)
        car_make = get_apparent_value(review_doc, 'car_make')
        car_model = get_apparent_value(review_doc, 'car_model')
        car_year = get_apparent_value(review_doc, 'car_year')
        purchase_date = get_apparent_value(review_doc, 'purchase_date')
        sentiment = get_apparent_value(review_doc, 'sentiment', 'neutral')
        results.append(DealerReview(id=review_doc["id"], name=review_doc["name"], dealership=review_doc["dealership"], 
                                    review=review_doc["review"], purchase=review_doc["purchase"], purchase_date=purchase_date, 
                                    car_make=car_make, car_model=car_model, car_year=car_year, 
                                    sentiment=sentiment))
    return results



# Add Review Method
def post_review_from_cf(url, dealer_id, review_obj):
    results = []
    # Call get_request with a URL parameter
    payload = {
        "IAM_API_KEY": credentials["IAM_API_KEY"],
        "COUCH_URL": credentials["COUCH_URL"],
        "dealerId": dealer_id,
        "reviewObject": review_obj,
        "method": "post"
    }
    json_result = cloud_function(url, payload)
    print('POST_REVIEW_JSON_RESULT: ')
    print(json_result)
    print('AFTER_POST_REVIEW_JSON_RESULT: ')
    return json_result


# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(text):
    response = natural_language_understanding.analyze( \
        html="<html><head><title>Review</title></head><body><h1>Review</h1><p>review: " + text + "</p></body></html>", \
        features=Features(emotion=EmotionOptions(targets=['review']))).get_result()
    print("NLU_RESPONSE")
    print(response)
    emotion_obj = response["emotion"]["document"]["emotion"]
    if emotion_obj["joy"] > 0.50:
        return "positive"
    if emotion_obj["fear"] > 0.30 or emotion_obj["anger"] > 0.30 or emotion_obj["disgust"] > 0.30 or emotion_obj["sadness"] > 0.30:
        return "negative"
    return "neutral"  