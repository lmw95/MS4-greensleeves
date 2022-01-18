from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number',
                       'date',
                       'delivery_cost',
                       'order_total',)

    list_display = ('order_number',
                    'date',
                    'full_name',
                    'street_address1',
                    'postcode',
                    'email',
                    'order_total',
                    'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)