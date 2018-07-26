from .models import application
import django_filters

class applicationsfilter(django_filters.FilterSet):
    class Meta:
        model = application
        fields = ['applicant', 'location', 'recommending_officer']