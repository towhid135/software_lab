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
                username1 = request.POST.get("username1")
                address1 = request.POST.get("address1")
                phone1 = request.POST.get("phone1")
                email1 = request.POST.get("email1")
                achi1 = request.POST.get("achi1")
                objective1 = request.POST.get("objective1")
                exp1 = request.POST.get("exp1")
                userobj = models.user(field = field1 ,username=username1, address = address1, phone = phone1, email = email1, image = img1, achievement = achi1, objective = objective1, exp = exp1)
                # print("true")
                userobj.save()
                return render(request, "user.html")
        return render(request,"user.html")

@login_required
def skill(request):
    if (request.method == 'POST'):
        soft1 = request.POST.get("soft1")
        tech1 = request.POST.get("tech1")
        org1 = request.POST.get("org1")
        cp1 = request.POST.get("cp1")
        lang1 = request.POST.get("lang1")

        skillobj = models.skill(soft=soft1, technical=tech1, organizational=org1, computer=cp1, language=lang1)
        # print("true")
        skillobj.save()
        return render(request, "skill.html")
    return render(request, "skill.html")

@login_required
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
@login_required
def employer(request):
        if (request.method == 'POST'):
                name = request.POST.get("name")
                address = request.POST.get("address")
                employerobj = models.employer(company_name = name, company_address=address)
                # print("true")
                employerobj.save()
                return render(request, "employer.html")
        return render(request,"employer.html")

@login_required
def addpsc(request):
    if (request.method == 'POST'):
        pscl = request.POST.get("sname")
        gpa = request.POST.get("gpa")
        board = request.POST.get("board")
        year = request.POST.get("year")
        pscinfo = models.PSC(pschool=pscl, p_GPA=gpa, p_board=board, p_year=year)
        pscinfo.save()
        return render(request, "addpsc.html")
    return render(request, "addpsc.html")

@login_required
def addjsc(request):
        if (request.method == 'POST'):
                jscl = request.POST.get("jname")
                gpa = request.POST.get("gpa")
                board = request.POST.get("board")
                year = request.POST.get("year")
                jscinfo = models.JSC(jschool=jscl, j_GPA=gpa, j_board =board, j_year=year)
                jscinfo.save()
                return render(request, "addjsc.html")
        return render(request, "addjsc.html")

@login_required
def addssc(request):
        if (request.method == 'POST'):
                scl = request.POST.get("name")
                grp=  request.POST.get("grp")
                gpa = request.POST.get("gpa")
                board = request.POST.get("board")
                year = request.POST.get("year")
                info = models.SSC(sschool=scl, s_group=grp, s_GPA=gpa, s_board =board, s_year=year)
                info.save()
                return render(request, "addssc.html")
        return render(request, "addssc.html")

@login_required
def addhsc(request):
        if (request.method == 'POST'):
                scl = request.POST.get("name")
                grp=  request.POST.get("grp")
                gpa = request.POST.get("gpa")
                board = request.POST.get("board")
                year = request.POST.get("year")
                info = models.HSC(hschool=scl, h_group=grp,  h_GPA=gpa, h_board =board, h_year=year)
                info.save()
                return render(request, "addhsc.html")
        return render(request, "addhsc.html")

@login_required
def addhonours(request):
    if (request.method == 'POST'):
        uni = request.POST.get("uni")
        prgm = request.POST.get("prgm")
        cgpa = request.POST.get("gpa")
        year = request.POST.get("year")
        info = models.Honours(ho_university=uni,ho_program=prgm, ho_CGPA=cgpa, ho_year=year)
        info.save()
        return render(request, "addhonours.html")
    return render(request, "addhonours.html")

@login_required
def addmasters(request):
    if (request.method == 'POST'):
        uni = request.POST.get("name")
        prgm = request.POST.get("prgm")
        cgpa = request.POST.get("gpa")
        year = request.POST.get("year")
        info = models.Masters(m_university=uni,m_program=prgm, m_CGPA=cgpa, m_year=year)
        info.save()
        return render(request, "addmasters.html")
    return render(request, "addmasters.html")
@login_required
def addphd(request):
    if (request.method == 'POST'):
        uni=request.POST.get("name")
        field = request.POST.get("name")
        year = request.POST.get("year")
        info = models.PHD(uni=uni,field=field,phd_year=year)
        info.save()
        return render(request, "addphd.html")
    return render(request, "addphd.html")


@login_required
def results(request):
    return render (request,'results.html')
