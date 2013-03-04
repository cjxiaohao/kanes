import registration
import registration.backends.simple
from django.core.urlresolvers import reverse

class KanesBackend ( registration.backends.simple.SimpleBackend ):
    def post_registration_redirect(self, request, user):
        return ( "/_/" , (), {} )