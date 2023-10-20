from django.contrib import admin
from .models import Spent, Person, Income
# Register your models here.
admin.site.register(Spent)
admin.site.register(Person)
admin.site.register(Income)
