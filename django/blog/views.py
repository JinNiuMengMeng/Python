from django.http import HttpResponse
from django.template import loader, Context

# def homeee(request, uid):
# 	return HttpResponse("id is:%s"%uid)

def new(request):
	t = loader.get_template("index.html")
	c = Context({})
	return HttpResponse(t.render(c))
# url(r'^$', 'blog.views.home', name='home'),