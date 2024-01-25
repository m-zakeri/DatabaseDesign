from django import template
from apps.course import models

register = template.Library()


@register.simple_tag
def time_course(time):
    total_seconds = time.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)

    if hours != 0:
        return f'{hours}ساعت ' + f'{minutes}دیقه '
    return f'{minutes}دیقه '


@register.simple_tag
def is_like_course(course_id, user_id):
    try:
        models.CourseLikes.objects.get(course_id=course_id, user_id=user_id)
        return True
    except:
        return False


@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode is not None:
        querystring = urlencode.split('&')
        queryfilter = filter(lambda p: p.split('=')[0] != field_name, querystring)
        query = '&'.join(queryfilter)
        url = '{}&{}'.format(url, query)

    return url

