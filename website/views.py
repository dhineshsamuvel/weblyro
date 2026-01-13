from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import LeadForm
from .models import Lead, Project  # Import Lead and Project models
import requests
from django.contrib import messages  # To show flash messages
from django.views.decorators.cache import cache_page  # Import cache_page decorator

# -------------------------
# reCAPTCHA verification
# -------------------------
def verify_recaptcha(token):
    payload = {
        "secret": settings.RECAPTCHA_SECRET_KEY,
        "response": token,
    }
    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data=payload
    )
    result = response.json()
    return result.get("success") and result.get("score", 0) >= 0.5

# -------------------------
# Pages
# -------------------------
@cache_page(60 * 15)  # Cache for 15 minutes
def home(request):
    return render(request, "index.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def services(request):
    return render(request, "services.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def portfolio(request):
    projects = Project.objects.all().order_by("-created_at")  # Fetch projects from the database
    return render(request, "portfolio.html", {"projects": projects})  # Pass projects to the template


@cache_page(60 * 15)  # Cache for 15 minutes
def about(request):
    return render(request, "about.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def thank_you(request):
    return render(request, "thank_you.html")


# -------------------------
# Service Detail Pages
# -------------------------
@cache_page(60 * 15)  # Cache for 15 minutes
def website_design(request):
    return render(request, "services/website_design.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def shopify(request):
    return render(request, "services/shopify.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def wordpress(request):
    return render(request, "services/wordpress.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def redesign(request):
    return render(request, "services/redesign.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def speed(request):
    return render(request, "services/speed.html")


@cache_page(60 * 15)  # Cache for 15 minutes
def maintenance(request):
    return render(request, "services/maintenance.html")


# -------------------------
# Contact Page
# -------------------------
def contact(request):
    if request.method == "POST":
        # Handle reCAPTCHA verification
        token = request.POST.get("g-recaptcha-response")
        if not token or not verify_recaptcha(token):
            messages.error(request, "Captcha verification failed. Please try again.")
            return render(request, "contact.html")

        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()  # Save the form data

            # Send email notification
            send_mail(
                "New Contact Message - Weblyro Tech",
                f"""
New Contact Message

Name: {lead.name}
Email: {lead.email}
Phone: {lead.phone}

Message:
{lead.message}
""",
                settings.DEFAULT_FROM_EMAIL,
                ["weblyrotech@gmail.com"],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("/thank-you/")  # Redirect to thank you page
        else:
            messages.error(request, "Please correct the errors in the form.")
            return render(request, "contact.html", {"form": form})
    else:
        form = LeadForm()  # Create an empty form for GET request

    return render(request, "contact.html", {"form": form})


# -------------------------
# Get Quote Page
# -------------------------
def get_quote(request):
    if request.method == "POST":
        # Handle reCAPTCHA verification
        token = request.POST.get("g-recaptcha-response")
        if not token or not verify_recaptcha(token):
            messages.error(request, "Captcha verification failed. Please try again.")
            return render(request, "get_quote.html")

        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()  # Save the form data

            # Send email notification
            send_mail(
                "New Website Lead - Weblyro Tech",
                f"""
New Lead Received

Name: {lead.name}
Email: {lead.email}
Phone: {lead.phone}
Company: {lead.company}
Service: {lead.service}

Message:
{lead.message}
""",
                settings.DEFAULT_FROM_EMAIL,
                ["weblyrotech@gmail.com"],
                fail_silently=False,
            )

            messages.success(request, "Your request for a quote has been submitted!")
            return redirect("/thank-you/")  # Redirect to thank you page
        else:
            messages.error(request, "Please correct the errors in the form.")
            return render(request, "get_quote.html", {"form": form})
    else:
        form = LeadForm()  # Create an empty form for GET request

    return render(request, "get_quote.html", {"form": form})
