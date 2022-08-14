from django.shortcuts import render
from app import models 
def home (request):
    banner = models.Banner.objects.filter(is_active=True).first()
    sites = models.Site.objects.filter(is_active=True).first()
    services = models.Service.objects.filter(is_active=True).order_by("order")[:6]
    return render(request, "app/main.html", locals())

def service(request):
    return render(request, 'app/service.html')
def contact(request):
    return render(request, 'app/contact.html')