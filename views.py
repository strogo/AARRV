from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from github_lib import *

def home(request):
    testText = "Testing text"
    t = get_template('home_template.html')
    html = t.render(Context({'hello': testText, 'num_watchers': numWatchers('opengovernment'), 'num_contrib': numCoders('opengovernment')}))
    return HttpResponse(html)
