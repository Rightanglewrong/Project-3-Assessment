from django.shortcuts import redirect, render
from django.views.generic import DeleteView
from django.db.models import Sum
from .forms import WidgetForm
from .models import Widget



# Create your views here.
def home(request):
    widgets_list = Widget.objects.all()
    t = Widget.objects.all().aggregate(Sum('quantity'))
    widget_form = WidgetForm()
    return render(request, 'home.html', {'widgets_list': widgets_list, 'widget_form': widget_form, 't':t})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')
    
class DeleteWidget(DeleteView):
    model = Widget
    success_url = '/'