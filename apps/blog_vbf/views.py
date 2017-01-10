from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Postt
#Create your views here.

class PosttForm(ModelForm):
    class Meta:
        model = Postt
        fields = ['titulo', 'cuerpo']

def postt_list(request, template_name='blog_vbf/blog_list.html'):
    postt = Postt.objects.all()
    data = {}
    data['object_list'] = postt
    return render (request,template_name, data)

def postt_create(request, template_name='blog_vbf/blog_form.html'):
    form = PosttForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_vbf:blog_list')
    return render(request, template_name, {'form':form})

def postt_update(request, pk, template_name='blog_vbf/blog_form.html'):
    print ("alalslsl")
    postt = get_object_or_404(Postt, pk=pk)
    form = PosttForm(request.POST or None, instance= postt)
    if form.is_valid():
        form.save()
        return redirect('blog_vbf.blog_list')
    return render(request, template_name, {'form':form})

def postt_delete(request,pk, template_name='blog_vbf/blog_confirm_delete.html'):
    postt=get_object_or_404(Postt, pk=pk)
    if request.method=='POST':
        postt.delete()
        return redirect('blog_vbf:blog_list')
    return render(request, template_name,{'object':postt})

