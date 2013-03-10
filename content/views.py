from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pdb import set_trace as bp
from .forms import WriteForm
from .models import Content

def home ( request ):
    return HttpResponseRedirect ( reverse ( "content_write" ) )

def all ( request ):
    context = {\
        "contents": Content.objects.filter ( user = request.user )
    }
    return render ( request, "content/all.html", context )

def view ( request, user, path ):
    user = User.objects.get ( username = user )
    path = not path and "/" or path
    
    try:
        content = Content.objects.get ( user = user, slug = path )
    except Content.DoesNotExist:
        if request.user:
            if not request.user == user:
                raise Http404
        
        return _write ( request, path )
    if not content.public:
        if not content.user == request.user:
            raise Http404

    context = {\
        "user": user,
        "path": path,
        "content": content,
        "is_markdown": content.syntax == "MARKDOWN",
    }
    return render ( request, "content/view.html", context )

def revision ( request, user, path ):
    pass

def _write ( request, path ):
    path = not path and "/" or path
    initial = { "slug": path }

    try:
        content = Content.objects.get ( user = request.user, slug = path )
    except Content.DoesNotExist:
        content = None

    if request.method == "POST":
        initial.update ( request.POST.dict ( ) )
        write_form = WriteForm ( initial, instance = content )
        if write_form.is_valid ( ):
            write_form.instance.user = request.user
            write_form.save ( )

            return HttpResponseRedirect ( \
                reverse ( "content_view", \
                          args = ( request.user.username, \
                                   write_form.cleaned_data['slug'], ) ) )
    else:
        write_form = WriteForm ( initial = initial, instance = content )

    context = {\
        "write_form": write_form,
    }
    return render ( request, "content/write.html", context )


@login_required
def write ( request, path ):
    return _write ( request, path )
