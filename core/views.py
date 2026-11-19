from django.shortcuts import render
from .data import THREATS, SAFETY_TIPS, CATEGORIES

def home(request):
    return render(request, "core/home.html", {
        "threat_count": len(THREATS),
        "tip_count": len(SAFETY_TIPS),
        "category_count": len(CATEGORIES),
        "featured_threats": THREATS[:3],
    })

def threats(request):
    return render(request, "core/threats.html", {"threats": THREATS})

def tips(request):
    return render(request, "core/tips.html", {"tips": SAFETY_TIPS})

def about(request):
    return render(request, "core/about.html")