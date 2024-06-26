from django import template

register = template.Library()

@register.filter
def discounted_price(Product):
    return Product.get_discounted_price()
