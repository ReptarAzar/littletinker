from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from web.models import Project, ProjectImage


def hacks(request, perm = None):
    permalink = perm
    return render_to_response('hacks.html',locals(),context_instance=RequestContext(request))

def one_project(request, id):
    project = Project.objects.get(id=id)
    images = ProjectImage.objects.filter(projectId = id)
    return render_to_response('one_project.html',locals(),context_instance=RequestContext(request))

def contact_us(request):
    if request.method == 'POST':
        send_mail('New #TinkerMessage from ' + request.POST['name'], request.POST['message'], request.POST['email'], ['info@littletinker.co'], fail_silently=False)
        return HttpResponseRedirect("/")
    else:
        return render_to_response('contact.html',locals(),context_instance=RequestContext(request))