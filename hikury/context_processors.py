from home.models import Home

def home_menu(request):
	home = Home.objects.get(pk=1)
	
	return{'home':home}