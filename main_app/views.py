from django.shortcuts import render, reverse
from .models import Widget
from django.forms import ModelForm
from main_app.models import Widget
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from django.http import HttpResponse

# Create your views here.

def widget_index(request, widget_id):
  widget = Widget.objects.get(id=widget_id)
  # instantiate FeedingForm to be rendered in the template
  Widget_form = WidgetForm()
  return render(request, 'index.html', {
  'widget': widget, 'widget_form': widget_form
  })

  class WidgetList(ListView):
    model = Widget

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
  success_url = 'index.html'

class WidgetUpdate(UpdateView):
  model = Widget
  fields = ['__all__']
  success_url = 'index.html'

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/index.html'

def index(request):
    return render (request, 'index.html')

def widgets_index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', { 'widgets': widgets })