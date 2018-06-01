"""
Definition of models.
"""
from django.db import models
from django.core.validators import RegexValidator


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

    name = models.CharField(
        max_length=20, choices=CHAPTER_CHOICES)
    status = models.CharField(max_length=20)
    school = models.CharField(max_length=50)
    contact_info = models.OneToOneField(
        'ContactInformation', on_delete=models.CASCADE)

    def __str__(self):
        return self.get_name_display() + ' ' + self.school

    @staticmethod
    def _bootstrap(count=25, local='en'):
        from mimesis import Business
        import random

        business = Business(local)
        contacts = ContactInformation.objects.all()

        for _ in range(count):
            try:
                chapter = Chapter(
                    name = random.choice(Chapter.CHAPTER_CHOICES),
                    status = "status",
                    school = business,
                    contact_info = random.choice(contacts)
                )
                chapter.save()
            except:
                continue

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
    relationship = models.CharField(
        max_length=25, choices=RELATIONSHIP_CHOICES)
    chapter = models.ForeignKey('Chapter', on_delete=models.DO_NOTHING)
    church = models.ForeignKey('MemberChurch', on_delete=models.DO_NOTHING)
    contact_info = models.OneToOneField(
        'ContactInformation', on_delete=models.CASCADE)

    STATUS_CHOICES = (('1', 'Active'),
                      ('2', 'Inactive'),
                      ('3', 'Alumni'))
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES)
    activation_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    submitted_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.sir_name

    @staticmethod
    def _bootstrap(count=500, local='en'):
        from mimesis import Person, Datetime
        import random

        person = Person(local)
        date = Datetime(local)
        chapters = Chapter.objects.all()
        churches = MemberChurch.objects.all()
        contact = ContactInformation.objects.all()

        for _ in range(count):
            try:
                member = Member(
                    first_name=person.name(),
                    sir_name=person.surname(),
                    relationship=random.choice(Member.RELATIONSHIP_CHOICES),
                    chapter=random.choice(chapters),
                    church=random.choice(churches),
                    contact_info=random.choice(contact),
                    status=random.choice(Member.STATUS_CHOICES),
                    activation_date=date.datetime(), # Time Zone problem when creating 
                    submitted_date=date.datetime()
                )
                member.save()
            except:
                continue

class MemberChurch(models.Model):
    SYNOD_CHOICES = (('1', 'LCMS'),
                     ('2', 'ELCA'),
                     ('3', 'NALC'),
                     ('4', 'WELS'),
                     ('5', 'OTHER'))
    name = models.CharField(max_length=50)
    pastor = models.CharField(max_length=50)
    synod = models.CharField(
        max_length=5, choices=SYNOD_CHOICES)
    contact_info = models.OneToOneField(
        'ContactInformation', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.get_synod_display()

    @staticmethod
    def _bootstrap(count=50, local='en'):
        from mimesis import Person, Business
        import random
        business = Business(local)
        person = Person(local)
        contact = ContactInformation.objects.all()

        for _ in range(count):
            try:
                church = MemberChurch(
                    name=business.company(),
                    pastor=person.full_name(),
                    synod=random.choice(MemberChurch.SYNOD_CHOICES),
                    contact_info=random.choice(contact)
                )
                church.save()
            except:
                continue


class ContactInformation(models.Model):
    street_name = models.CharField(max_length=50)
    street_number = models.IntegerField()
    zip_code = models.IntegerField()
    state = models.CharField(max_length=2)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()

    def __str__(self):
        return str(self.street_number) + ' ' + self.street_name + ' ' + self.state

    @staticmethod
    def _bootstrap(count=500, locale='en'):
        from mimesis import Person, Address
        person = Person(locale)
        address = Address(locale)

        for _ in range(count):
            contact = ContactInformation(
                street_name=address.street_name(),
                street_number=address.street_number(),
                zip_code=address.zip_code(),
                state=address.state(),
                email=person.email(),
                phone_number=person.telephone()
            )

            contact.save()
