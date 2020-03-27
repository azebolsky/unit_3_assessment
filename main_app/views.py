from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    if request.method == 'POST':
        widget_form = WidgetForm(request.POST)
        if widget_form.is_valid():
            widget_form.save()
        return redirect('/')
    return render(request, 'index.html', {
        'widgets': widgets, 'widget_form': widget_form
    })

def delete(request, pk):
    delete_widget = Widget.objects.get(id=pk)
    delete_widget.delete()
    return redirect('/')