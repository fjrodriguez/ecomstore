from django.shortcuts import render_to_response

def home(request):
    return render_to_response("index.htmldjango")
# vim: set et ai ts=4 sw=4: 
