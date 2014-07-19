from django.shortcuts import render
from django.http import HttpResponse
from models import Note


def index(request):
    notes = [note for note in Note.objects.all()]
    return render(request, 'index.html', {'notes': notes})
#    return HttpResponse("\n".join(notes), content_type="text/plain")
