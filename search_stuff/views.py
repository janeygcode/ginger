from django.shortcuts import render
from search_stuff.models import Stuff
from django.db.models import Q
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import connections


# Create your views here.
def stuff_index(request):
	all_stuff = Stuff.objects.all()

	if request.method == 'POST':
		name = request.POST.get('name')

		cursor = connections['default'].cursor()

		sql = "INSERT INTO search_stuff_stuff(name) VALUES('%s')" % name
		cursor.executescript(sql)


	context = {
		'all_stuff': all_stuff
	}
	return render(request, 'index.html', context)



def waf_stuff_index(request):
	all_stuff = Stuff.objects.all()

	if request.method == 'POST':
		name = request.POST.get('name')

		cursor = connections['default'].cursor()

		sql = "INSERT INTO search_stuff_stuff(name) VALUES('%s')" % name
		cursor.executescript(sql)


	context = {
		'all_stuff': all_stuff
	}
	return render(request, 'waf_index.html', context)




def stuff_detail(request, pk):
	stuff = Stuff.objects.get(pk=pk)
	context = {
		'stuff':stuff
	}
	return render(request, 'stuff_detail.html', context)


def search(request):
	# query = request.GET['q']
	# sql = f"SELECT * FROM stuff WHERE name LIKE '%{query}%';"

	query = request.GET.get('q')

	sql = "SELECT * FROM search_stuff_stuff WHERE name LIKE '%{query}%'"

	# object_list = Stuff.objects.filter(
	# 	Q(name__icontains=query))

	object_list = Stuff.objects.raw(f"SELECT * FROM search_stuff_stuff WHERE name LIKE '%{query}%'")



	context = {
		'query':query,
		'object_list':object_list,
	}
	return render(request, 'search_results.html', context)

