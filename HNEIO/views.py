from django.shortcuts import render


# Create your views here.

def home( request ):
  if not request.user.is_authenticated:
    return render( request, 'login.html' )
  return render( request, 'index.html' )