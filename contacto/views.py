from django.shortcuts import render, redirect  
from contacto.forms import ContactoForm  
from contacto.models import Contacto  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = ContactoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ContactoForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    contactos = Contacto.objects.all()  
    return render(request,"show.html",{'contactos':contactos})  
def edit(request, id):  
    contacto = Contacto.objects.get(id=id)  
    return render(request,'edit.html', {'contacto':contacto})  
def update(request, id):  
    contacto = Contacto.objects.get(id=id)  
    form = ContactoForm(request.POST, instance = contacto)  
    # return redirect("/show?" + str(id)) 
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'contacto': contacto})  
def destroy(request, id):  
    contacto = Contacto.objects.get(id=id)  
    contacto.delete()  
    return redirect("/show")  
