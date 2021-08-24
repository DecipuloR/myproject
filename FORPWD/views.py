from django.shortcuts import render, redirect, get_object_or_404
from .models import  Applicants, React, Post 
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.list import ListView



class SomeSuperuserView(SuperuserRequiredMixin, TemplateView):
    template_name = "applicants/applicants.html"


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('login')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="signUp.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):

    messages.info(request, "You have successfully logged out.") 
    return redirect("login")



def register(request): 
    applicants = Applicants.objects.all()
    context = {"applicants":applicants}
    return render(request, 'Regspage.html', context)

def pwd(request):
    applicant = Applicants(
        firstName=request.POST['firstName'],
        lastName=request.POST['lastName'],
        middleName=request.POST['middleName'],
        disability=request.POST['disability'], 
        Address=request.POST['Address'], 
        Age=request.POST['Age'], 
        Gender=request.POST['Gender'], 
        ContactNumber=request.POST['ContactNumber'], 
        BirthDate=request.POST['BirthDate'], 
        File=request.POST['2x2File'], 
        COIFile=request.POST['COIFile'],
        MCFile=request.POST['MCFile'],

        )
    applicant.save()
    return redirect('/home')

def editinfo(request, id):
    applicants = Applicants.objects.get(id=id)
    context = {'applicants': applicants}
    return render(request, 'info.html', context)

def updateinfo(request, id):
    applicant = Applicants.objects.get(id=id)
    applicant.firstName = request.POST['firstName']
    applicant.lastName = request.POST['lastName']
    applicant.middleName = request.POST['middleName']
    applicant.disability = request.POST['disability']
    applicant.Address = request.POST['Address']
    applicant.Age = request.POST['Age']
    applicant.Gender = request.POST['Gender']
    applicant.ContactNumber = request.POST['ContactNumber']
    applicant.BirthDate = request.POST['BirthDate']
    applicant.File = request.POST['File']
    applicant.COIFile = request.POST['COIFile']
    applicant.MCFile = request.POST['MCFile']
    applicant.save()
    return redirect('/applicants')

def deleteinfo(request, id):
    applicant = Applicants.objects.get(id=id)
    applicant.delete()
    return redirect('/applicants')


def Home(request):

    return render(request, 'Main.html')


def aboutus(request):
    return render (request, 'aboutus.html')


def Adminpage(request):
    applicants = Applicants.objects.all()
    context = {'applicants': applicants}
    return render(request,'applicants.html', context)

def statusurl(request, id):
    applicant = Applicants.objects.all()

    return render(request, 'status.html', {'applicant': applicant})

def editstatus(request,id):

    applicant = Applicants.objects.get( id=id)
    applicant.status=request.POST['statusresult'] 
    applicant.Pwdnumber=request.POST['Pwdnumber']
    applicant.save()
     
    return redirect('/applicants')


def Announcement(request):
    
    msg = React.objects.all()
    post = Post.objects.all()

   
    context = { 'msg':msg, 'post':post}
    return render (request, 'announcements.html', context)


def commentSaving(request):

    comment = React(
        message=request.POST['message'],
        )
    comment.save()
    return redirect('/news')

def Poster (request):
    postt = Post.objects.all()
    context = { 'postt': postt }
    return render(request, 'base/head.html', context)


def Postii(request):
    postt = Post( PostAnnouncement = request.POST['PostAnnouncement'],)
    postt.save()
    return redirect('/news')

# def updatePost(request, id):
#     postt = Post.objects.get(id=id)
#     context = {'postt':postt}

#     return render(request, 'postupdate.html', context)


# def editPost(request, id):
#     edit = Post.objects.get(id=id)
#     post.PostAnnouncement = request.POST['PostAnnouncement']
#     edit.save()
#     return redirect('/news')

def announce(request):
    return render(request, 'adminpost.html')


class SearchView(ListView):
    model = Applicants
    template_name = 'cashgift.html'
    context_object_name = 'all_search_results'
    context_object_name = 'applicants'

    def get_queryset(self):

        applicants = Applicants.objects.all()
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Applicants.objects.filter(firstName__contains=query)
            result = postresult
        else:
           result = None
        return result


def cashGift(request):

    applicant = Applicants.objects.all().order_by('BirthDate')
    
    context = {'applicant':applicant}
    return render(request, 'cashgift.html', context)

def cgcheker(request, id):

    applicant = Applicants.objects.all()
    context = {'applicant':applicant}
    return render(request, 'CGchecker.html', context)

def cashGiftUpdate(request,id):

    applicant = Applicants.objects.get(id=id)
    applicant.cash = request.POST['cash']
    applicant.save()
    return redirect('/cashgift')
















 # data = Member.objects.get(id=id)
    # info = Applicants.objects.get(id=data.pwdinfo_id)
    # statuss = StatusForm(instance= data)
    # form = StatusForm()
    # if request.method == 'Post':
    #         form = StatusForm(request.POST, instance=data)
    #         if form.is_valid():
    #                 form.save()
    #                 return redirect('/applicants')


# def index(request):
#     members = Member.objects.all()
#     context = {'members': members}
#     return render(request, 'base/index.html', context)

# def create(request):
#     member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
#     member.save()
#     return redirect('/about')

# def edit(request, id):
#     members = Member.objects.get(id=id)
#     context = {'members': members}
#     return render(request, 'base/edit.html', context)

# def update(request, id):
#     member = Member.objects.get(id=id)
#     member.firstname = request.POST['firstname']
#     member.lastname = request.POST['lastname']
#     member.save()
#     return redirect('/about')

# def delete(request, id):
#     member = Member.objects.get(id=id)
#     member.delete()
#     return redirect('/about')





