from django.shortcuts import render



def index(request):
	return render (request, "posts/index.html")

def our_menu(request):
	return render (request, "posts/our_menu.html")




