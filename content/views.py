from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import WriteForm

def home ( request ):
    return HttpResponse ( "" )

def write ( request ):
    if request.method == "POST":
        write_form = WriteForm ( request.POST )
        if write_form.is_valid ( ):
            write_form.save ( )
            return HttpResponseRedirect ( "/" )
    else:
        write_form = WriteForm ( )
    return render ( request, "content/write.html" )
