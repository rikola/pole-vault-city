import datetime

from django.db import models


class Pole(models.Model):
    brand = models.CharField(max_length=100)
    inches = models.IntegerField()
    weight = models.IntegerField()
    purchased_at = models.DateField(blank=True, null=True)

    def is_rented(self):
        return False

    def age(self):
        purchased = self.purchased_at.value_from_object(datetime.datetime)
        return datetime.date.today() - purchased

    def __str__(self):
        return f'{self.brand} - {self.inches} - {self.weight}'


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def get_rentals(self):
        return

    def __str__(self):
        return self.name


class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    pole = models.ForeignKey(Pole, on_delete=models.DO_NOTHING)
    checkout = models.DateField()
    due = models.DateField()
    returned = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comment = models.TextField(max_length=300, blank=True, null=True)

    def active(self) -> bool:
        return self.returned is None

    def overdue(self) -> bool:
        if self.returned:
            return True
        return datetime.datetime.now() > self.due

    def __str__(self):
        c = self.customer.name
        p = self.pole.brand
        l = self.pole.inches
        return f"{c} - {p} - {l}"
