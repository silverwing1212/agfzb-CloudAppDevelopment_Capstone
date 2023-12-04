import requests
import json
# import related models here
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth

credentials = {
    "IAM_API_KEY": "4iKJcQaT1ZJq6tbnwC4TZIqUwAoLz4UjLA7RBEm01OGN",
    "COUCH_URL": "https://3c366aa0-e65a-45df-b3a8-94d6d0482251-bluemix.cloudantnosqldb.appdomain.cloud"
}

iam_token = "eyJraWQiOiIyMDIzMTEwNzA4MzYiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjYwMDNNS0lFIiwiaWQiOiJJQk1pZC02NjYwMDNNS0lFIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiZjMyN2E2ZWMtOGQxMC00NWFiLWE0YTUtZGUzMzFiOTQxNWRkIiwiaWRlbnRpZmllciI6IjY2NjAwM01LSUUiLCJnaXZlbl9uYW1lIjoiS3lsZSIsImZhbWlseV9uYW1lIjoiSHVtcGhyZXkiLCJuYW1lIjoiS3lsZSBIdW1waHJleSIsImVtYWlsIjoia3lsZXVuaXZlcnNpdGllc0BnbWFpbC5jb20iLCJzdWIiOiJreWxldW5pdmVyc2l0aWVzQGdtYWlsLmNvbSIsImF1dGhuIjp7InN1YiI6Imt5bGV1bml2ZXJzaXRpZXNAZ21haWwuY29tIiwiaWFtX2lkIjoiSUJNaWQtNjY2MDAzTUtJRSIsIm5hbWUiOiJLeWxlIEh1bXBocmV5IiwiZ2l2ZW5fbmFtZSI6Ikt5bGUiLCJmYW1pbHlfbmFtZSI6Ikh1bXBocmV5IiwiZW1haWwiOiJreWxldW5pdmVyc2l0aWVzQGdtYWlsLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJkZmU1NDFmMDMxZjA0YzhmYTU0OTU2ZjRlYWRmYmZjNiIsImltc191c2VyX2lkIjoiMTE1OTQ5NzYiLCJmcm96ZW4iOnRydWUsImltcyI6IjI3NjQxOTIifSwiaWF0IjoxNzAxNjk0NjI0LCJleHAiOjE3MDE2OTgyMjQsImlzcyI6Imh0dHBzOi8vaWFtLmNsb3VkLmlibS5jb20vaWRlbnRpdHkiLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.EM5BtmP6ear_lzxwC6k5P6BugBxmj6wJ1b6_OH-281hOBM889KmXk1pAi0x9JxOJxuymou3QnGnF8CfrDik4JMQrn4KVRxAlnWLsxow3IXBzIx4j95HslVhND_sDYUcg0PInM8KbhUo7nxjLd1oluqHbxcdwwxBAdx-GbZpBU0Xtdud08t9IswMdmOFXPweA52h9v3wa310tDP7c0wr5Cs06Y9BcKTmAfMO3df3G-3yv8mTTfkcPZsxby7YeMXMZz8TE93P1vlT60HwVv8rHNZg_9dq4qXgImOcDhuD1sIlZNaYbDePqbGI7L3XuFi9B7Qs_UTLStiSeuRxq7Nktmw"
authorization = "Bearer " + iam_token

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
    return post_request(url, json_payload)['response']['result']

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


# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



