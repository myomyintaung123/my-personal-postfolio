from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs, Internship


# Create your views here.
def home(request):
    return render(request, "home.html")


def handleblog(request):
    posts = Blogs.objects.all()
    context = {"posts": posts}
    return render(request, "handleblog.html", context)


def about(request):
    return render(request, "about.html")


def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login  to access this page!")
        return redirect("/auth/login/")
    if request.method == "POST":
        fname = request.POST.get("name")
        fusn = request.POST.get("usn")
        femail = request.POST.get("email")
        fcollege = request.POST.get("cname")
        foffer = request.POST.get("offer")
        fstartdate = request.POST.get("startdate")
        fenddate = request.POST.get("enddate")
        fprojectreport = request.POST.get("projectreport")

        # python upper case method
        fname = fname.upper()
        fusn = fusn.upper()
        fcollege = fcollege.upper()
        fprojectreport = fprojectreport.upper()
        foffer = foffer.upper()

        check1 = Internship.objects.filter(usn=fusn)
        check2 = Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request, "Your Details Have Stored Already!")
            return redirect("/internshipdetails")

        query = Internship(
            fullname=fname,
            usn=fusn,
            email=femail,
            college_name=fcollege,
            offer_status=foffer,
            start_date=fstartdate,
            end_date=fenddate,
            project_report=fprojectreport,
        )
        query.save()
        messages.success(request, "Form Is Submitted Successful!")
        return redirect("/internshipdetails")

    return render(request, "intern.html")


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        fphoneno = request.POST.get("num")
        fdescription = request.POST.get("desc")
        query = Contact(
            name=fname, email=femail, phone_number=fphoneno, description=fdescription
        )
        query.save()
        messages.success(request, "Thanks for contacting us. We will get by soon...!")
        return redirect("/contact")
    return render(request, "contact.html")


def error_404(request, exception):
    return render(request, "handle404.html")
