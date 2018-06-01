from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Member
from .models import Chapter
from .models import MemberChurch
from .models import ContactInformation


def chapter(request):
    try:
        chapters = Chapter.objects.order_by('id')
        context = {'chapter_list': chapters}
        return render(request, 'chapter/chapter_index.html', context)
    except:
        raise Http404('No Chapters to show')


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


def chapter_members(request, chapter_id):
    return

def member(request):
    #try:
        members = Member.objects.order_by('id')
        context = {'member_list': members}
        return render(request, 'chapter/member_index.html', context)
    # except:
    #     raise Http404('No Members found')


def member_detail(request, member_id):
    return HttpResponse('Member Detail' + str(member_id))


def member_contact(request, member_id):
    return HttpResponse('member contact' + str(member_id))
