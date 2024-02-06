from django.utils import timezone

from apps.course.models import Course
from apps.course.models import CouponCode
from .models import Order


class Cart:

    def __init__(self, request):
        self.session = request.session

        cart = request.session.get('cart')
        if not cart:
            cart = request.session['cart'] = {}

        self.cart = cart

    def __iter__(self):
        for item in self.cart.values():
            item['course'] = Course.objects.get(id=item['course_id'])
            yield item

    def add(self, course):
        slug = course.slug
        if slug not in self.cart:
            self.cart[slug] = {'course_id': course.id, 'price': course.apply_discount()}

        self.save()

    def remove(self, slug):
        if slug in self.cart:
            del self.cart[slug]

            self.save()

    def remove_cart(self):
        self.cart.clear()
        self.save()

    def total_price(self):
        total = 0
        for item in self.cart.values():
            total += item['price']
        return total

    def save(self):
        self.session.modified = True


def apply_coupon(request, name_discount, order_id):
    coupon = CouponCode.objects.filter(name=name_discount)
    order = Order.objects.get(id=order_id)
    text_message = ''
    final_price = 0
    now = timezone.now()

    if not coupon.exists() or not coupon[0].is_active:
        text_message = 'There is no discount code with this name'

    elif request.user in coupon[0].user_costumer.all():
        text_message = 'You have already used this code'

    elif order.is_discount:
        text_message = 'You cannot use more than one discount code for an order'


    elif not coupon[0].valid_from <= now <= coupon[0].valid_to or coupon[0].number_discount == 0:
        text_message = 'The discount code is not valid'

    else:

        for obj in order.items.all():
            price = obj.final_price
            if obj.course in coupon[0].course.all():
                discount = coupon[0].discount
                price = price - ((price * discount) / 100)

            final_price += price
        coupon[0].user_costumer.add(request.user)
        coupon[0].number_discount -= 1
        coupon[0].save()
        text_message = f'{coupon[0].discount}% discount has been successfully applied'

    return text_message, final_price
