from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    # 2.
    
    return render(request, 'accounts/auth_form.html', context)
    
def login(request):
    #1.
    
    return render(request, 'accounts/auth_form.html', context)
    
def logout(request):
    # 3.
    return redirect('posts:list')