from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note_tag = request.POST.get('tag')
        try:
            tag = Tag.objects.get(tag=note_tag)
        except Tag.DoesNotExist:
            tag = Tag(tag=note_tag)
            tag.save()       
        if (title and content and tag):
            note = Note(title=title, content=content, tag=tag)
            note.save()
        return redirect('index')    
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        note = Note.objects.filter(id=id)
        note.delete()
        return redirect('index')

def edit(request):
    if request.method == 'POST':
        id = request.POST.get('id').replace('/', '')
        id = int(id)
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note.objects.filter(id=id)[0]
        note.__dict__.update({'title': title, 'content': content})
        note.save()
        return redirect('index')
    else:
        id = request.GET.get('id')  
        note = Note.objects.filter(id=id)
        return render(request, 'notes/edit.html', {'note': note[0]})

def tag_list(request):
    if request.method == 'GET':
        all_tags = Tag.objects.all()
        return render(request, 'notes/tag_list.html', {'tags': all_tags})

def all_notes_with_tag(request):
    if request.method == 'GET':
        tag_list = list(request.GET.items())
        tag = tag_list[0][1]
        notes_with_tag = Note.objects.filter(tag__tag=tag)
        return render(request, 'notes/all_notes_with_tag.html', {'notes': notes_with_tag})
    else:
        return redirect('index')