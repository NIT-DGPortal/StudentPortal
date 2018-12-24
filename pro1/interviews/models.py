from django.db import models

STATUS_CHOICES = (
    ('OPEN', 'Open'),
    ('CLOSED', 'Closed'),
)


class Department(models.Model):
    depatment_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.depatment_name}"


class Internship(models.Model):
    company_name = models.CharField(max_length=50)
    department = models.ManyToManyField(Department)
    job_designation = models.CharField(max_length=50)
    qualification_needed = models.CharField(max_length=20)
    last_date_to_apply = models.DateField()
    test_location = models.TextField(default='')
    salary_offered = models.CharField(max_length=20)
    person_of_contact = models.CharField(max_length=20)
    email_id = models.EmailField()
    phone_no = models.CharField(max_length=12)
    form_link = models.URLField(default='')
    status = models.CharField(max_length=6, choices=STATUS_CHOICES,
                              default='OPEN')
    other_details = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.company_name}"

    def departments(self):
        return ",".join([d.depatment_name for d in self.department.all()])


class Placement(models.Model):
    company_name = models.CharField(max_length=50)
    expected_salary = models.CharField(max_length=20)
    job_designation = models.CharField(max_length=50)
    qualification_needed = models.CharField(max_length=20)
    last_date_to_apply = models.DateField()
    department = models.ManyToManyField(Department)
    form_link = models.URLField(default='')
    status = models.CharField(max_length=5, choices=STATUS_CHOICES,
                              default='OPEN')
    interview_or_test_location = models.TextField()
    additional_documents = models.TextField()
    additional_information = models.TextField(default=None, null=True,
                                              blank=True)

    def __str__(self):
        return f"{self.company_name}"

    def departments(self):
        return ",".join([d.depatment_name for d in self.department.all()])
