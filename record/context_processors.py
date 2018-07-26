from .models import application,staff


def allcontexts(request):
    applications = application.objects.all()
    staffs = staff.objects.all()
    residential = application.objects.filter(type_of_use='Residential')
    residential_len = len(residential)
    commercial = application.objects.filter(type_of_use='Commercial')
    commercial_len = len(commercial)
    recreational = application.objects.filter(type_of_use='Recreational')
    recreational_len = len(recreational)
    mixed = application.objects.filter(type_of_use='Mixeduse')
    mixed_len = len(mixed)
    industrial = application.objects.filter(type_of_use='Industrial')
    industrial_len = len(industrial)
    applications_length = len(applications)
    staff_length = len(staffs)
    context = {'staff_length': staff_length, 'applications_length': applications_length, 'residential_len': residential_len, 'commercial_len': commercial_len, 'recreational_len': recreational_len, 'mixed_len': mixed_len,'industrial_len': industrial_len }
    return context