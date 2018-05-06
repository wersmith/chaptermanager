from django.contrib import admin
from .models import Member
from .models import MemberChurch
from .models import Chapter
from .models import ContactInformation

admin.site.register(Member)
admin.site.register(MemberChurch)
admin.site.register(Chapter)
admin.site.register(ContactInformation)
