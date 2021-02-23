from django.db import models


# создание модели питомца
class Pet(models.Model):

    TYPES = (
        ('Кошка', 'Кошка'),
        ('Собака', 'Собака'),
        ('Попугай', 'Попугай'),
    )

    GENDER = (
        ('мальчик', 'мальчик'),
        ('девочка', 'девочка'),
    )
    pet_type = models.CharField(max_length=16, choices=TYPES, verbose_name="Вид питомца", blank=False)
    name = models.CharField(max_length=100, verbose_name="Кличка")
    gender = models.CharField(max_length=8, choices=GENDER, verbose_name="Пол", blank=True)
    breed = models.CharField(max_length=250, verbose_name="Порода", default="Беспородный")
    color = models.CharField(max_length=128, verbose_name="Окрас")
    avatar = models.ImageField(upload_to='images', blank=True, verbose_name="Фото")
    age = models.SmallIntegerField(verbose_name="Возраст", default='Неизвестно')
    # date_of_entry = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата поступления")
    date_of_entry = models.DateField(verbose_name="Дата поступления")
    # anonse = models.CharField(max_length=250, blank=True, verbose_name="Коротко о питомце")
    about = models.TextField(verbose_name="О питомце", blank=True)

    def __str__(self):
        return self.name
