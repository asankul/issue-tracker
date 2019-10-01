from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from webapp.models import ToDo
from webapp.forms import ToDoListForm


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
