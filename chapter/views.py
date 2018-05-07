from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Member
from .models import Chapter
from .models import MemberChurch
from .models import ContactInformation


def chapter(request):
    chapters = Chapter.objects.order_by('id')
    result = ', '.join([c.get_name_display() for c in chapters])
    return HttpResponse(result)


def chapter_detail(request, chapter_id):
    try:
        chapter = Chapter.objects.get(pk=chapter_id)
    except:
        raise Http404('Chapter not found.')
    return HttpResponse('Chapter Detail: ' + chapter.get_name_display() + ' at ' + chapter.school)


def chapter_contact(request, chapter_id):
    try:
        chapter = Chapter.objects.get(pk=chapter_id)
    except:
        raise Http404('Chapter not found.')
    return HttpResponse('Chapter Contact info: ' + chapter.contact_info.email)


def member(requests):
    return HttpResponse('Member endpoint')


def member_detail(request, member_id):
    return HttpResponse('Member Detail' + str(member_id))


def member_contact(request, member_id):
    return HttpResponse('member contact' + str(member_id))
