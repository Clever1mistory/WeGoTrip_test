from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    content = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('PROCESSING', 'В обработке'),
        ('CONFIRMED', 'Подтвержден'),
    )

    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PROCESSING')
    creation_time = models.DateTimeField(auto_now_add=True)
    confirmation_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Заказ  №{self.id}"


class Payment(models.Model):
    STATUS_CHOICES = (
        ('PAID', 'Оплачено'),
        ('PROCESSING', 'В обработке'),
        ('DECLINED', 'Отменено'),
    )

    PAYMENT_TYPES = (
        ('CARD', 'Карта'),
        ('CASH', 'Наличные'),
    )

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PROCESSING')
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPES)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')

    def __str__(self):
        return f"Оплата заказа №{self.order.id}"
