from django.shortcuts import render, redirect
from polls.forms import PessoasForms
from polls.models import Pessoas


def index(request):
    data = {}
    data['form'] = PessoasForms()
    return render(request, 'index.html', data)


def cadastro(request):
    data = {}
    data['db'] = Pessoas.objects.all()
    return render(request, 'cadastro.html', data)


def create(request):
    form = PessoasForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro')


def edit(request, pk):
    data = {}
    data['db'] = Pessoas.objects.get(pk=pk)
    data['form'] = PessoasForms(instance=data['db'])
    return render(request, 'index.html', data)


def update(request, pk):
    data = {}
    data['db'] = Pessoas.objects.get(pk=pk)
    form = PessoasForms(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('cadastro')

def delete(request, pk):
    db = Pessoas.objects.get(pk=pk)
    db.delete()
    return redirect('cadastro')