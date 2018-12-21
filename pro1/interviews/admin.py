from django.contrib import admin
from .models import Internship, Department, Placement

# Register your models here.


class InternshipAdmin(admin.ModelAdmin):
    list_display = ('company_name',
                    'departments',
                    'job_designation',
                    'qualification_needed',
                    'last_date_to_apply',
                    'test_location',
                    'salary_offered',
                    'person_of_contact',
                    'email_id',
                    'phone_no',
                    'other_details',)


class PlacementAdmin(admin.ModelAdmin):
    list_display = ('company_name',
                    'expected_salary',
                    'departments',
                    'job_designation',
                    'qualification_needed',
                    'last_date_to_apply',
                    'interview_or_test_location',
                    'additional_documents',
                    'additional_information',)


admin.site.register(Department)
admin.site.register(Internship, InternshipAdmin)
admin.site.register(Placement, PlacementAdmin)
