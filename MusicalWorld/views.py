from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'MusicalWorld/Home.html')
    else:
        redirect(request,)

class UserFormView(View):
    form_class = UserForm
    template_name ='MusicalWorld/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('Music:index')
        return render(request, self.template_name, {'form':form})
