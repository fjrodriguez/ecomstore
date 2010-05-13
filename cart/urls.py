from django.conf.urls.defaults import *

urlpatterns = patterns('ecomstore.cart.views',
        (r'^$', 'show_cart', {'template_name': 'cart/cart.htmldjango'},
            'show_cart'),
        )
# vim: set ai ts=4 et sw=4 sts=4: 
