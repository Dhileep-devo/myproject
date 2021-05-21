from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import FeedFile
from .forms import FeedModelForm,FileModelForm

...
def create_to_feed(request):
    user = request.user
    if request.method == 'POST':
        print('post request')
        form = FeedModelForm(request.POST)
        file_form = FileModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('file') #field name in model
        if form.is_valid() and file_form.is_valid():
            feed_instance = form.save(commit=False)
            feed_instance.user = user
            print(feed_instance.user)
            feed_instance.save()
            for f in files:
                file_instance = FeedFile(file=f, feed=feed_instance)
                file_instance.save()
            return redirect('/')
    else:
        form = FeedModelForm()
        file_form = FileModelForm()
        return render(request,'login.html',{'form':form,'file_form':file_form})