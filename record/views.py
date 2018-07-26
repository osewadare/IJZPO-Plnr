from django.shortcuts import render
from .models import application, staff
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView
from .filters import applicationsfilter
from django.urls import reverse_lazy

class indexview(ListView):
    model = application
    context_object_name = 'applications'
    template_name = 'record/index.html'
    queryset = application.objects.all().order_by('-id')[:3]

class applicationsview(ListView):
    model = application
    context_object_name = 'applications'
    template_name = 'record/applications.html'
    paginate_by = 10
    queryset = application.objects.all()

class applicationupdate(UpdateView):
    model = application
    fields = ['sn', 'date_of_registration', 'applicant', 'location', 'registration_plan_number', 'type_of_use', 'no_of_floors', 'amount', 'treasury_receipt_number', 'inspector', 'recommending_officer', 'charting_officer', 'approving_officer', 'luc_no']
    success_url = '../applications'

class applicationdelete(DeleteView):
    model = application
    success_url = reverse_lazy('records:applications')


class mapsview(TemplateView):
    template_name = 'record/maps.html'


class CreateApplication(CreateView):
    model = application
    fields = ['sn', 'date_of_registration', 'applicant', 'location', 'registration_plan_number', 'type_of_use', 'no_of_floors', 'amount', 'treasury_receipt_number', 'inspector', 'recommending_officer', 'charting_officer', 'approving_officer', 'luc_no']
    success_url = '../applications'

def search(request):
    applications = application.objects.all()
    application_filter = applicationsfilter(request.GET, queryset=applications)
    return render(request, 'record/search.html', {'filter': application_filter})


class staffview(ListView):
    template_name = 'record/staff.html'
    model = staff
    context_object_name = 'staffs'

class AddStaff(CreateView):
    model = staff
    template_name = 'record/add_staff.html'
    fields = '__all__'
    context_object_name = 'form'
    success_url = reverse_lazy('records:staff_profile')