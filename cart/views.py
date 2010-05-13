from django.shortcuts import render_to_response
from django.template import RequestContext
from ecomstore.cart import cart
from django.core import urlresolvers
from ecomstore.cart import cart
from django.http import HttpResponseRedirect
from ecomstore.catalog.forms import ProductAddToCartForm


def show_cart(request, template_name="cart/cart.htmldjango"):
    cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    return render_to_response(template_name, locals(),
            context_instance=RequestContext(request))

def show_product(request, product_slug, 
        template_name="catalog/product.htmldjango"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.all()
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart...create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        # check if posted data is valid
        if form.is_valid():
            # add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        # it's a GET, create the unbound form. Note request as a kwarg
        form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()
    return render_to_response("catalog/product.htmldjango", locals(),
            context_instance=RequestContext(request))


# vim: set ai ts=4 et sw=4 sts=4: 
