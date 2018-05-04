"""
Definition of models.
"""

from django.db import models


class Chapter(models.Model):
    CHAPTER_CHOICES = (('1', 'Alpha'),
                       ('2', 'Beta'),
                       ('3', 'Delta'),
                       ('4', 'Epsilon'),
                       ('5', 'Zeta'),
                       ('6', 'Eta'),
                       ('7', 'Iota'),
                       ('8', 'Nu'),
                       ('9', 'Omega'),
                       ('10', 'Alpha-Alpha'))
    name = models.CharField(max_length=20, choices=CHAPTER_CHOICES, default="N/A")
    status = models.CharField(max_length=20, help_text="chapter")
    school = models.CharField(max_length=50)
    contact_info = models.OneToOneField('ContactInformation', on_delete=models.CASCADE)


class Member(models.Model):
    RELATIONSHIP_CHOICES = (('1', 'Brother'),
                            ('2', 'Pledge'),
                            ('3', 'President'),
                            ('4', 'Vice President'),
                            ('5', 'Tresurer'),
                            ('6', 'Sargent-at-Arms'),
                            ('7', 'Secretary'),
                            ('8', 'Social-Chair'),
                            ('9', 'Philantropy-Chair'),
                            ('10', 'Recruitment-Chair'),
                            ('11', 'Pledge-Education-Chair'))
    first_name = models.CharField(max_length=20, help_text="Enter first name")
    sir_name = models.CharField(max_length=20, help_text="Enter last name")
    relationship = models.CharField(max_length=25, choices=RELATIONSHIP_CHOICES)
    chapter = models.OneToOneField('Chapter', on_delete=models.CASCADE)
    church = models.OneToOneField('MemberChurch', on_delete=models.CASCADE)
    contact_info = models.OneToOneField('ContactInformation', on_delete=models.CASCADE)


class MemberActivation(models.Model):
    STATUS_CHOICES = (('1', 'Active'),
                      ('2', 'Inactive'),
                      ('3', 'Alumni'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="N/A")
    activation_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    member = models.OneToOneField('Member', on_delete=models.CASCADE)


class MemberChurch(models.Model):
    SYNOD_CHOICES = (('1', 'LCMS'),
                     ('2', 'ELCA'),
                     ('3', 'NALC'),
                     ('4', 'WELS'),
                     ('5', 'OTHER'))
    name = models.CharField(max_length=50, default="N/A")
    pastor = models.CharField(max_length=50, default="N/A")
    synod = models.CharField(max_length=5, choices=SYNOD_CHOICES, default="N/A")
    contact_info = models.OneToOneField('ContactInformation', on_delete=models.CASCADE)


class ContactInformation(models.Model):
    street_name = models.CharField(max_length=50)
    street_number = models.IntegerField()
    zip_Code = models.IntegerField()
    state = models.CharField(max_length=2)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
