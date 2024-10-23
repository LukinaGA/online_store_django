from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, template_name='home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спаисбо за обращение, {name}!")

    return render(request, template_name='contacts.html')
