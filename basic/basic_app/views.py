from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'
class OfficeListView(ListView):
    model = models.Office

class OfficeDetailView(DetailView):
    context_object_name = 'office_details'
    model = models.Office
    template_name = 'basic_app/office_detail.html'

class OfficeCreateView(CreateView):
    fields = '__all__'
    model = models.Office


class OfficeUpdateView(UpdateView):
    fields = ("name","address","dept")
    model = models.Office
class OfficeDeleteView(DeleteView):
    model = models.Office
    success_url = reverse_lazy("basic_app:list")
