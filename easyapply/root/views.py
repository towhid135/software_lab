from django.shortcuts import render, redirect
from django.http import HttpResponse
from root import models
from django.db.models import Subquery
from django.views.generic import TemplateView
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

class Home(TemplateView):
    template_name = 'home.html'

@login_required
def dashboardView(request):
    return render (request,'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def user(request):
        if (request.method == 'POST'):
                img1 = request.FILES.get("img1")
                field1 = request.POST.get("field1")
                address1 = request.POST.get("address1")
                phone1 = request.POST.get("phone1")
                email1 = request.POST.get("email1")
                achi1 = request.POST.get("achi1")
                objective1 = request.POST.get("objective1")
                exp1 = request.POST.get("exp1")
                userobj = models.user(field = field1 , address = address1, phone = phone1, email = email1, image = img1, achievement = achi1, objective = objective1, exp = exp1)
                # print("true")
                userobj.save()
                return render(request, "user.html")
        return render(request,"user.html")
