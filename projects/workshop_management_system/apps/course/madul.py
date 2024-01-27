def filter_course(request, queryset):
    categories = request.GET.getlist('categories')
    languages = request.GET.getlist('languages')
    levels = request.GET.getlist('levels')
    price = request.GET.get('price')
    search = request.GET.get('q')
    sort = request.GET.get('sort')

    if categories and 'all' not in categories:
        queryset = queryset.filter(category__name__in=categories).distinct()
    if languages:
        queryset = queryset.filter(language__name__in=languages).distinct()
    if levels:
        queryset = queryset.filter(level__in=levels)

    if price and price != 'all':
        if price == 'free':
            queryset = queryset.filter(price=0)
        else:
            queryset = queryset.exclude(price=0)
    if search:
        queryset = queryset.filter(name__icontains=search)
    if sort and sort != 'all':
        if queryset == 'update':
            queryset = queryset.order_by('-updated_at')
        else:
            queryset = queryset.order_by('-number_customer')

    return queryset
