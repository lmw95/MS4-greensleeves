from django import template
from datetime import date, timedelta, datetime

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


# https://stackoverflow.com/questions/6871016/adding-days-to-a-date-in-python
@register.filter(name='calc_estimated_delivery')
def calc_estimated_delivery(days):
    """Calculate estimated delivery day"""
    return date.today() + timedelta(days=days)
