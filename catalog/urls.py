from django.conf.urls.defaults import *

urlpatterns = patterns('ecomstore.catalog.views',
        (r'^$', 'index', {'template_name':'catalog/index.htmldjango'},
            'catalog_home'),
        (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
            {'template_name':'catalog/category.htmldjango'}, 
            'catalog_category'),
        (r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',
            {'template_name': 'catalog/product.htmldjango'},
            'catalog_product'),
        )

# vim: set ai ts=4 et sw=4 sts=4: 
