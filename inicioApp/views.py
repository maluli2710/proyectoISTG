from django.shortcuts import render

from inicioApp.models import Usuario, Trabajador


# Create your views here.
def inicioDef(request):
    return render(request, 'inicio.html', {})

def paginaDef(request):
    return render(request,'pagina.html',{})

def loginSesionDef(request):
    if request.method=='GET':
        return render(request, 'inicio.html', {})
    else:
        usuarioStr=request.POST.get('userInTx')
        passwordStr=request.POST.get('passwordInPs')
        try:
           usuario=Usuario.objects.get(usuario=usuarioStr, password=passwordStr)
           trabajadorList= Trabajador.objects.values()
           return render(request,"menu.html",{"list": trabajadorList,"usuarioStr": usuario.usuario})
        except Usuario.DoesNotExist:
            return render(request, "inicio.html",{"err":"Usuario o contraseña no son correctos"})
