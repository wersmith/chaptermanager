from django.db import models

# Create your models here.
class Chapter(models.Model):
    # Fields
    CHAPTER_CHOICES = (Alpha, Beta, Delta, Epsilon, Zeta, Eta, Iota, Nu, Omega, Alpha-Alpha )
    chapter_name = models.CharField(max_length=20, choices=CHAPTER_CHOICES, default="N/A")
    chapter_status = models.CharField(max_length=20, help_text="chapter")



    # Methods

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name










class Member(models.Model):
    # Fields
    first_name = models.CharField(max_length=20, help_text="Enter first name")
    last_name = models.CharField(max_length=20, help_text="Enter last name")
    home_street_address = models.CharField(max_length=50, help_text="Enter Home Address")
    chapter = Foreign



    # Methods

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name