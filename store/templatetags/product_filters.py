from django import template

register = template.Library()

@register.filter
def get_discounted_price(product):
    return product.get_discounted_price()
