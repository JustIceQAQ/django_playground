from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from iris.forms import IrisModelForm
from iris.models import Iris


# https://www.learncodewithmike.com/2020/04/django-class-based-views.html
class IrisListView(ListView):
    model = Iris

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = IrisModelForm()  # 資料模型表單
        return context


class IrisCreateView(CreateView):
    model = Iris
    form_class = IrisModelForm
    success_url = '/iris'


class IrisUpdateView(UpdateView):
    model = Iris
    form_class = IrisModelForm
    success_url = '/iris'
    queryset = Iris.objects.all()


class IrisDeleteView(DeleteView):
    model = Iris
    success_url = '/iris'


def iris_func(request):
    dataset = Iris.objects.filter(classification="setosa")

    return HttpResponse("QAQ")
