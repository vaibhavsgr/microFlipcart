from django import template

register = template.Library()

@register.filter(name='order_price_history')
def orderPriceHistoryLookup(d, key):
    if key in d:
        return d[key]
    else:
        return ("   ")
