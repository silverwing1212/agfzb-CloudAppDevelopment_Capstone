from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarModel
from .restapis import get_dealer_reviews_from_cf, get_dealers_from_cf, post_review_from_cf, analyze_review_sentiments
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            return render(request, 'djangoapp/index.html', context)
    return render(request, 'djangoapp/index.html', context)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
def registration_request(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exists = False
        try:
            User.objects.get(username=username)
            user_exists = True
        except:
            """pass"""
        if not user_exists:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            return redirect('djangoapp:index')
        return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    url = "https://us-east.functions.cloud.ibm.com/api/v1/namespaces/046716ff-e42a-4d60-a2f6-18db643765ba/actions/api/dealership?blocking=true"
    dealerships = get_dealers_from_cf(url)
    context["dealership_list"] = dealerships
    return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...
def get_dealer_details(request, dealer_id):
    context = {}
    url = "https://us-east.functions.cloud.ibm.com/api/v1/namespaces/046716ff-e42a-4d60-a2f6-18db643765ba/actions/api/review?blocking=true"
    reviews = get_dealer_reviews_from_cf(url, dealer_id)
    for review in reviews:
        review_text = review.review
        sentiment = analyze_review_sentiments(review_text)
        review.sentiment = sentiment
    context["dealer_id"] = dealer_id
    context["review_list"] = reviews
    return render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
def add_review(request, dealer_id):
    if request.method == 'GET':
        context = {}
        cars = []
        cars_res = CarModel.objects.filter(dealerId=dealer_id)
        print("CAR_RES")
        print(cars_res)
        cars_first = CarModel.objects.filter(dealerId=dealer_id).first()
        print("CAR_FIRST")
        print(cars_first)
        cars = cars_res
        context["dealer_id"] = dealer_id
        context["cars"] = cars
        return render(request, 'djangoapp/add_review.html', context)
    if request.method == 'POST':
        review_obj = {}
        review = request.POST['review']
        purchased = request.POST['purchasecheck'] == 'on'
        user = request.user
        review_obj["name"] = user.first_name + ' ' + user.last_name
        review_obj["review"] = review
        review_obj["purchase"] = purchased
        review_obj["dealership"] = dealer_id
        if purchased:
            car_id = request.POST['car']
            purchasedate = request.POST['purchasedate']
            car = CarModel.objects.filter(pk=car_id).get()
            review_obj["car_make"] = car.carMake.name
            review_obj["car_model"] = car.name
            review_obj["car_year"] = car.year.strftime("%Y")
            review_obj["'purchase_date': "] = purchasedate
        print('REVIEW_OBJ')
        print(review_obj)
        print('AFTER_REVIEW_OBJ')
        url = "https://us-east.functions.cloud.ibm.com/api/v1/namespaces/046716ff-e42a-4d60-a2f6-18db643765ba/actions/api/review?blocking=true"
        context = {}
        context["dealer_id"] = dealer_id
        post_review_from_cf(url, dealer_id, review_obj)
        return redirect('djangoapp:index')