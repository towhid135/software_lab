from django.shortcuts import render
from django.http import HttpResponse
from root import models
from django.db.models import Subquery

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

def circular(request):
        if (request.method == 'POST'):
                title = request.POST.get("title")
                description = request.POST.get("description")
                salary = request.POST.get("salary")
                requirements = request.POST.get("requirements")
                date = request.POST.get("date")
                circularobj = models.circular( title = title, description = description, salary = salary, requirements = requirements, date = date)
                # print("true")
                circularobj.save()
                return render(request, "circular.html")
        return render(request,"circular.html")

def employer(request):
        if (request.method == 'POST'):
                name = request.POST.get("name")
                address = request.POST.get("address")
                employerobj = models.employer(company_name = name, company_address=address)
                # print("true")
                employerobj.save()
                return render(request, "employer.html")
        return render(request,"employer.html")

