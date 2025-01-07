from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from django.core.mail import EmailMessage, send_mail
# from YoBawarchi import settings
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
# from . tokens import generate_token

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("dashboard")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )

def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'dashboard.html')

def offer(request):
    return render(request, 'offer.html')

def emergency(request):
    return render(request, 'emergency.html')

def offers(request):
    return render(request, 'offers.html')

def feedback(request):
    return render(request, 'feedback.html')

def orderhistory(request):
    return render(request, 'orderhistory.html')

def profile_management(request):
    return render(request, 'profile_management.html')

def loyalty(request):
    return render(request, 'loyalty.html')

def dashboard(request):
    return render(request, 'dashboard.html')


oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)
