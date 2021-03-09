# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Movie


class MovieListView(ListView):
    """Show all movies."""

    model = Movie


class MovieDetailView(DetailView):
    """Show the requested movie."""
    
    model = Movie

    def get_object(self, queryset=None):
        return Movie.objects.get(id=self.kwargs.get("id"))

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except:
            return redirect('movies:index')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class MovieCreateView(CreateView):
    """Create a new movie."""

    model = Movie
    fields = [
        'title',
        'year',
        'rated',
        'released_on',
        'genre',
        'director',
        'plot',
    ]
    error_message = 'The creation has failed'
    success_message = 'The movie created successfully'

    def form_valid(self, form):
        self.object = form.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, self.error_message)
        return super().form_invalid(form)


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    """Update the requested movie."""

    model = Movie
    fields = [
        'title',
        'year',
        'rated',
        'released_on',
        'genre',
        'director',
        'plot',
    ]

    success_message = 'The movie updated successfully'
    error_message = 'The update has failed'
    
    def get_object(self, queryset=None):
        return Movie.objects.get(id=self.kwargs.get("id"))

    def get(self, request, *args, **kwargs):
        
        try:
            self.object = self.get_object()
        except:
            return redirect('movies:index')
        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        messages.add_message(self.request, messages.ERROR, self.error_message)
        return self.render_to_response(self.get_context_data(form=form))



class MovieDeleteView(DeleteView):
    """Delete the requested movie."""

    model = Movie
    success_url = reverse_lazy('movies:index')

    def get_object(self, queryset=None):
        return Movie.objects.get(id=self.kwargs.get("id"))

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except:
            return redirect('movies:index')
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
            messages.add_message(request, messages.SUCCESS, 'The movie deleted successfully')
        except:
            messages.add_message(request, messages.ERROR, 'The deletion has failed')

        return redirect('movies:index')