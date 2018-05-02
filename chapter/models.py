from django.db import models

# Create your models here.
class ChapterInfo(models.Model):
    # Fields
    CHAPTER_CHOICES = ('Alpha', 'Beta', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Iota', 'Nu', 'Omega', 'Alpha-Alpha')
    chapter_name = models.CharField(max_length=20, choices=CHAPTER_CHOICES, default="N/A")
    chapter_status = models.CharField(max_length=20, help_text="chapter")


class ActivationInfo(models.Model):
    activation_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    class_number =  models.AutoField()
    submitted_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    chapter = models.ForeignKey('ChapterInfo', on_delete=models.CASCADE)



class MemberChurchInfo(models.Model):
    SYNOD_CHOICES = ('LCMS', 'ELCA', 'NALC', 'WELS', 'OTHER')

    church_name = models.CharField(max_length=50, default="N/A")
    home_pastor = models.Charfield(max_length=50, default="N/A")
    church_address = models.Charfield(max_length=50, default="N/A")
    church_state = models.CharField(max_length=2, default="N/A")
    church_zip = models.CharField(max_length=5, default="N/A")
    church_synod = models.CharField(max_length=5, choices = SYNOD_CHOICES, default="N/A")



class Member(models.Model):
    # Fields
    STATUS_CHOICES = ('Active', 'Inactive', 'Alumni')

    first_name = models.CharField(max_length=20, help_text="Enter first name")
    last_name = models.CharField(max_length=20, help_text="Enter last name")
    home_street_address = models.CharField(max_length=50, help_text="Enter Home Address")
    chapter = models.ForeignKey('ChapterInfo', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="N/A")
    church_info = models.ForeignKey('MemberChurchInfo', on_delete=models.CASCADE)
