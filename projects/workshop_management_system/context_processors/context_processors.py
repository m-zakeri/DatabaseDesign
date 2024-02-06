from apps.course.models import CourseCategory


def categories(request):
    categories = CourseCategory.objects.filter(is_publish=True)
    return {'categories': categories}
