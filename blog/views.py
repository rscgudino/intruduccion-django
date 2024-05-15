from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'blog_list.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, 'blog_list.html', context)

#//////////////////////////////////////////////////////////////

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            # Procesar el formulario si es válido
            form.save()
            # Redirigir a una página de éxito o cualquier otra acción
        context = {'form': form}
        return render(request, 'blog_create.html', context)
