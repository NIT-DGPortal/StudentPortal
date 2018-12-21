from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Placement, Internship
# Create your views here.


@login_required(redirect_field_name='')
def home(request):
    internship = Internship.objects.all()
    placement = Placement.objects.all()
    return render(request, 'interviews/home.html',
                  {'internships': internship, 'placements': placement},)


@login_required
def internship(request, internship_id):
    internship_object = get_object_or_404(Internship, id=internship_id)
    return render(request, 'interviews/internship.html',
                  {'internship': internship_object},)


@login_required
def placement(request, placement_id):
    placement_object = get_object_or_404(Placement, id=placement_id)
    return render(request, 'interviews/placement.html',
                  {'placement': placement_object},)
