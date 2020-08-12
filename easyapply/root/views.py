from django.shortcuts import render
from django.http import HttpResponse
from root import models
from django.db.models import Subquery

def user(request):
        if (request.method == 'POST'):
                img1 = request.POST.get("img1")
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

def addphd(request):
    if (request.method == 'POST'):
        field = request.POST.get("name")
        year = request.POST.get("year")
        info = models.PHD(field=field,phd_year=year)
        info.save()
        return render(request, "addphd.html")
    return render(request, "addphd.html")


