from django.shortcuts import render
from bestapp.models import Hydjobs, Punejobs, Bngjobs


# Create your views here.
def homepage_view(request):
    return render(request, 'bestapp/input.html')


def hydjobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'bestapp/hydjobs.html', my_dict)

def punejobs_view(request):
    jobs_list = Punejobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'bestapp/punejobs.html', my_dict)

def bngjobs_view(request):
    jobs_list = Bngjobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'bestapp/bngjobs.html', my_dict)
