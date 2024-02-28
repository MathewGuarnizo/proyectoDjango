from django.shortcuts import render, HttpResponse,  redirect

# Create your views here.
def holaMundo (request):
    return render(request,'holaMundo.html')

def saludo (request,redirigir = 0):
    nombre = 'Mathew Guarnizo'
    return render(request,'cantacto.html',{
        'texto':' ',
        'name':nombre,
        'nombres':['Mathew', 'Camila', 'Sebas', 'Kevin']
    })

def index (request):
    """
    template = "
                        <h1> Inicio </h1>
                        <p> Años desde el 2024 hasta 2050 </p>
                        <ul>
                        "
    year = 2024
    while year <= 2050:
        template += f"<li>{str(year)}"
        if year %2==0:
            template += " (año par)"
        
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            template += " (año bisiesto)"
        template+="</li>"
        year += 1

    template += "</ul><hr>"
    """
    nombre = 'Mathew Guarnizo'
    years = list(range(2024, 2051))
    miLista = ['Archivo 1', 'Archivo 2', 'Archivo 3']

    while len(miLista) < 10:
        nuevoArchivo = f'Archivo {len(miLista) + 1}'
        miLista.append(nuevoArchivo)

    otraLista = [x for x in range(1, 6)]

    return render(request,'index.html',{
        'mi_variable': 'soy un dato que esta en la vista',
        'title':'Inicio de Sitio',
        'titulo':'Pagina de Inicio SENA',
        'name':nombre,
        'mi_lista': miLista, 
        'otra_lista': otraLista,
        })

def presentacion (request):
    # return HttpResponse(layout+"""
    #                     <h2> Nombre: Mathew Guarnizo <br> Numero: 3126542790 <br> Email: guarnizo.reyes.mathew@gmail.com </h2>
    #                     """)
    return render(request,'presentacion.html')

def contacto (request):
    nombre='Mathew Guarnizo',
    return render(request,'contacto.html',{
        'name':nombre,
        'nombres':['Mathew', 'Camila', 'Sebas', 'Kevin']
    })

def contactanos (request):
    return render(request,'contactanos.html')

def quienesSomos(request):
    return render(request,'quienesSomos.html')

def productos_Servicios(request):
    return render(request,'productos_Servicios.html')
