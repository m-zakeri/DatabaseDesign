from django.db.models import Sum


def filter(request, queryset):
    search = request.GET.get('q')
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    if category:
        if category != 'all':
            queryset = queryset.filter(course__category__name=category)

    if search:
        queryset = queryset.filter(user__username__icontains=search)

    if sort and sort != 'all':

        if sort == 'HighScore':
            queryset = queryset.order_by('-score')
        else:
            queryset = queryset.annotate(total_sales=Sum('course__number_customer')).order_by('-total_sales')

    return queryset
