from django.db.models import Sum


def filter_teacher(request, queryset):
    search = request.GET.get('q')
    category = request.GET.get('category')
    sort = request.GET.get('sort')

    if category:
        if category:
            queryset = queryset.filter(course__category__name__icontains=category)

    if search:
        queryset = queryset.filter(user__username__icontains=search)

    if sort :

        if sort == 'HighScore':
            queryset = queryset.order_by('-score')
        else:
            queryset = queryset.annotate(total_sales=Sum('course__number_customer')).order_by('-total_sales')

    return queryset
