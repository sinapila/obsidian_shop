from django import template
from jalali_date import date2jalali

register =template.Library()

@register.filter(name='shamsi_date')
def get_shamsi_create_date(val):
    return date2jalali(val)


@register.filter(name='shamsi_time')
def get_shamsi_create_time(val):
    return val.strftime('%H:%H')



@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + ' تومان'


@register.simple_tag
def multiply(quantity, price, *args, **kwargs):
    return three_digits_currency(quantity * price)
