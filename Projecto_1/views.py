from django.http import HttpResponse
import datetime
from django.template import Context, Template 


def saludar(request):
    return HttpResponse("Hola mundo!")

def segunda_vista(request):
    return HttpResponse('Ya entendi! Esto esta papita!!!')     

def dia_de_hoy(request):

    dia = datetime.datetime.today()
    cadena = 'Hoy es: ' + str(dia)
    return HttpResponse(cadena)

    #En HTML seria asi:
    #codigohtml = "<h1>Hoy es: " + str(dia) + "</h1>"  
    #return HttpResponse(codigohtml)   


def saludo_con_nombre(self, nombre):

    return HttpResponse("<h1>Hola mi nombre es: " + nombre + "</h1>"  )    


#Desafio Generico no Entregable

#¿En qué año naciste?

#Enviar por parametro tu edad y calcular el año de nacimiento (más o menos uno, para no entrar con los meses).


def calcular_nacimiento(self, age):

    year_today = int(datetime.datetime.now().year)
    age = int(age)
    edad = year_today - age

    return HttpResponse('<h1>Tu año de nacimento es ' + str(edad) + '</h1>')
    
    #edad = year_today - age

    #return HttpResponse("Tu edad es" + str(edad))        


def probando_html(self):
    mi_archivo = open('C:/Users/ricar/Documents/3_School_Stuff/CoderHouse/Curso_Python/Clase_17_Django_1/Projecto_1/Plantillas/template1.html') 
    #Este es el path de mi archivo template1.html, para manejarlo mas facil, lo pongo en una variable.
    
    plantilla = Template(mi_archivo.read()) #Leemos el archivo (mi_archivo.read()) y lo convierto en Template de Django, la cual guardo en mi variable plantilla
    mi_archivo.close() #Cierro el archivo

    #Aqui ya tengo mi Template de Django

    contexto = Context() #Creamos un contexto vacio -- Mas adelante veremos que es un contexto

    documento = plantilla.render(contexto)  #Mi documento final se arma renderizando  el contexto a la plantilla

    return HttpResponse(documento)