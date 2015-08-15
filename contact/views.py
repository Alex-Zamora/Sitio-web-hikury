from django.shortcuts import render, render_to_response
from django.template import RequestContext
from contact.forms import ContactForm
from django.core.mail import EmailMultiAlternatives  #Enviamos HTML

def contact_view(request):
	
	#Definir si se envio la informacion
	info_enviado = False 
	
	#Crear variables para cada campo de nuestro formulario
	nombre = None
	telefono = None
	email = None
	mensaje = None

	#Si request fue POST es por que alguien intento enviar informacion
	if request.method == 'POST':
		#guardamos nuestro formulario con la informacion del post
		form  = ContactForm(request.POST)
		#validamos la informacion del post
		if form.is_valid():
			#Si la informacion es correcta
			info_enviado = True
			#Rellenamos las variables
			nombre = form.cleaned_data['name']
			telefono = form.cleaned_data['telephone']
			email = form.cleaned_data['email']
			mensaje = form.cleaned_data['mensaje']

			#Configuracion enviando mensaje via Gmail
			#to_admin = 'wixarikalex@gmail.com'
			#html_content = "Informacion Recibida<br><br>Nombre: "+(nombre)+"<br><br>Telefono: "+(telefono)+"<br><br>email: "+(email)+"<br><br>Mensaje: "+(mensaje)
			#msj = EmailMultiAlternatives('Contacto Hikury', html_content, 'from@server.com', [to_admin])
			#msj.attach_alternative(html_content,'text/html') #Definimos el contenido como html
			#msj.send() #Se envia correo

	#Si no fue POST entonces fue GET		
	else:
		form = ContactForm()
	contexto = {'form':form, 'info_enviado':info_enviado, 'nombre':nombre}
	return render(request, 'contacto.html', contexto)
