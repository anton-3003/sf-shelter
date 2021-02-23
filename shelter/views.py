from django.shortcuts import render, loader
from .models import Pet
from .forms import PetForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


def index(request):
    template = loader.get_template('index.html')
    pets = Pet.objects.all()
    b_data = {
        "pets": pets,
    }
    return HttpResponse(template.render(b_data, request))


def contact(request):
    template = loader.get_template('contact.html')
    c_data = {
        "title": "Контакты",
        "e_mail": "contact@kindstep.ru",
        "phone_number": "+7 (987) 654 3210",
        "address": "Россия, г. Москва, ул. Иванова, д.5"
    }
    return HttpResponse(template.render(c_data, request))


def about(request):
    template = loader.get_template('about_us.html')
    c_data = {
        "title": "О нас",
        "about_text": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
            Odio quis, rem! Autem delectus dicta, excepturi iure labore minus, 
            modi neque nesciunt quam tempora tempore tenetur! 
            Alias consequatur labore reiciendis repellendus similique! 
            Aperiam autem, consectetur doloremque doloribus earum fugiat iste iusto non odit quod sint, 
            veniam vitae voluptate? A animi blanditiis consequatur cumque id illo impedit natus quasi quod totam! 
            At autem expedita porro quasi quos rem ullam. Ducimus excepturi facilis labore nobis.
            Dolor earum in nostrum odio, provident ullam unde? 
            Aliquam animi, aperiam aspernatur at atque consequatur dolor fugit illo ipsam, 
            iure maxime omnis perferendis possimus, quae quisquam quos reiciendis saepe? 
            A aliquid, architecto asperiores consequatur ducimus et ex itaque molestiae reprehenderit sed totam voluptate!
            Blanditiis, facere laborum magni modi nemo nostrum nulla numquam obcaecati quis voluptas voluptatibus?    
        """
    }
    return HttpResponse(template.render(c_data, request))


class PetDetail(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'pet'


class PetCreate(CreateView):
    model = Pet
    fields = '__all__'
    template_name = 'create.html'
    success_url = reverse_lazy('shelter:index')
