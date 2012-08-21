from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from web.models import Project, ProjectImage
from web.forms import ContactForm


def home(request):
    form = ContactForm()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


def about(request, perm=None):
    permalink = perm
    return render_to_response('about.html', locals(), context_instance=RequestContext(request))


def hacks(request, perm=None):
    permalink = perm
    return render_to_response('hacks.html', locals(), context_instance=RequestContext(request))


def one_project(request, id):
    project = Project.objects.get(id=id)
    urlPretty = project.url[7:-1]
    images = ProjectImage.objects.filter(projectId=id)
    return render_to_response('one_project.html', locals(), context_instance=RequestContext(request))


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail('New #TinkerMessage from ' + request.POST['name'], request.POST['message'], request.POST['email'], ['info@littletinker.co'], fail_silently=False)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    else:
        return render_to_response('contact.html', locals(), context_instance=RequestContext(request))
