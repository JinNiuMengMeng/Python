from django.http import HttpResponse

def homeee(request):
	return HttpResponse('hey, world')
# url(r'^$', 'blog.views.home', name='home'),