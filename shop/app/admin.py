import time

from django.contrib import admin
from django.utils import timezone

from .models import Order, Product, Payment
from .tasks import send_webhook_request


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'content', 'price']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'status', 'payment_type']
    list_filter = ['status', 'payment_type']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_amount', 'status', 'creation_time', 'confirmation_time']
    actions = ['confirm_order']

    def confirm_order(self, request, queryset):
        for order in queryset:
            try:
                payment = order.payment  # Получаем экземпляр Payment, связанный с Order
            except Payment.DoesNotExist:
                continue  # Если связанной оплаты нет, переходим к следующему заказу

            if payment.status == 'PAID':  # Проверяем статус оплаты
                order.status = 'CONFIRMED'
                order.confirmation_time = timezone.now()
                order.save()
                time.sleep(2)
                send_webhook_request.delay(order.id, str(order.total_amount), str(order.confirmation_time))

        self.message_user(request, "Выбранные заказы были успешно подтверждены.")
