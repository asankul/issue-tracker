from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from webapp.models import ToDo, Status, Type
from webapp.forms import ToDoListForm, StatusForm, TypeForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = ToDo.objects.all()
        return context


class TodoView(TemplateView):
    template_name = 'todolist_view.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['list'] = get_object_or_404(ToDo, pk=pk)
        return context


class ToDoListCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ToDoListForm()
        return render(request, 'todolist_add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            ToDo.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('index')
        else:
            return render(request, 'todolist_add.html', context={'form': form})


class ToDoListUpdateView(View):
    def get(self, request, *args, **kwargs):
        list = get_object_or_404(ToDo, pk=kwargs.get('pk'))
        form = ToDoListForm(data={
            'summary': list.summary,
            'description': list.description,
            'status': list.status_id,
            'type': list.type_id
        })
        return render(request, 'todolist_update.html', context={'form': form, 'list': list})

    def post(self, request, *args, **kwargs):
        list = get_object_or_404(ToDo, pk=kwargs.get('pk'))
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            list.summary = form.cleaned_data['summary']
            list.description = form.cleaned_data['description']
            list.status = form.cleaned_data['status']
            list.type = form.cleaned_data['type']
            list.save()
            return redirect('list_view', pk=list.pk)
        else:
            return render(request, 'todolist_update.html', context={'form': form, 'list': list})


class ToDoListDeleteView(View):
    def get(self, request, *args, **kwargs):
        list = get_object_or_404(ToDo, pk=kwargs.get('pk'))
        return render(request, 'delete.html', context={'list': list})

    def post(self, request, *args, **kwargs):
        list = get_object_or_404(ToDo, pk=kwargs.get('pk'))
        list.delete()
        return redirect('index')


class StatusView(TemplateView):
    template_name = 'status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = Status.objects.all()
        return context


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status_add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('index')
        else:
            return render(request, 'status_add.html', context={'form': form})


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        list = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(data={
            'name': list.name
        })
        return render(request, 'status_update.html', context={'form': form, 'list': list})

    def post(self, request, *args, **kwargs):
        list = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(data=request.POST)
        if form.is_valid():
            list.name = form.cleaned_data['name']
            list.save()
            return redirect('index')
        else:
            return render(request, 'status_update.html', context={'form': form, 'list': list})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        list = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(request, 'status_delete.html', context={'list': list})

    def post(self, request, *args, **kwargs):
        list = get_object_or_404(Status, pk=kwargs.get('pk'))
        list.delete()
        return redirect('index')


class TypeView(TemplateView):
    template_name = 'type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = Type.objects.all()
        return context


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type_add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                name=form.cleaned_data['name']
            )
            return redirect('index')
        else:
            return render(request, 'type_add.html', context={'form': form})


class TypeUpdateView(View):
    def get(self, request, *args, **kwargs):
        list = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(data={
            'name': list.name
        })
        return render(request, 'type_update.html', context={'form': form, 'list': list})

    def post(self, request, *args, **kwargs):
        list = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(data=request.POST)
        if form.is_valid():
            list.name = form.cleaned_data['name']
            list.save()
            return redirect('index')
        else:
            return render(request, 'type_update.html', context={'form': form, 'list': list})


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        list = get_object_or_404(Type, pk=kwargs.get('pk'))
        return render(request, 'type_delete.html', context={'list': list})

    def post(self, request, *args, **kwargs):
        list = get_object_or_404(Type, pk=kwargs.get('pk'))
        list.delete()
        return redirect('index')
