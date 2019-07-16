from django.shortcuts import render
from .forms import PollForm
from .models import Poll

# Create your views here.
def index(request):
    polls = Poll.objects.all().order_by('date')
    if request.method == 'POST':
        form = PollForm(request.POST)

        if form.is_valid():
            print('Form valid. saving...')
            form.save()
            form = PollForm()
            polls = Poll.objects.all().order_by('date')
            return render(request,'poll/index.html', {'form': form, 'polls': polls})
        print('There were errors in the form:')
        print(form.errors)
        return render(request,'poll/index.html', {'form': form, 'polls': polls})

    form = PollForm()
    return render(request,'poll/index.html', {'form': form, 'polls': polls})
