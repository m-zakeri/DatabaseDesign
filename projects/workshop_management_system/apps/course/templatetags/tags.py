from django import template

register = template.Library()


@register.simple_tag
def time_course(time):
    total_seconds = time.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)

    if hours != 0:
        return f'{hours}ساعت ' + f'{minutes}دیقه '
    return f'{minutes}دیقه '
