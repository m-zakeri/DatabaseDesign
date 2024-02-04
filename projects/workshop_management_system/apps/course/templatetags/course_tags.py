import datetime

from django import template
from apps.course import models

from jdatetime import datetime
from datetime import timezone
from django.utils import timezone as Timezone
from apps.course.madul import format_time

from persiantools.jdatetime import JalaliDate

register = template.Library()


@register.simple_tag
def time_course(time):
    total_seconds = time.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)

    if hours != 0 and minutes != 0:
        return f'{hours}ساعت ' + f'{minutes}دقیقه '
    elif hours != 0 and minutes == 0:
        return f'{hours}ساعت '
    return f'{minutes}دقیقه '


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


@register.simple_tag
def existence_variable(request, name, variable):
    lst = request.GET.getlist(name)

    if variable in lst:
        return True
    else:
        return False


@register.filter
def first_half(lst):
    first_half = len(lst) // 2
    return lst[:first_half]


@register.filter
def second_half(lst):
    second_half = len(lst) // 2
    return lst[second_half:]


@register.simple_tag
def permission_video(request, meeting_id, course_id):
    meeting = models.Meeting.objects.get(id=meeting_id)
    course = models.Course.objects.get(id=course_id)

    if meeting.free:
        return True
    elif not request.user.is_authenticated:
        return False

    elif course.customer.filter(user=request.user).exists():
        return True

    elif course.teacher.filter(user=request.user).exists():
        return True
    return False


@register.simple_tag
def license_course(request, course_id):
    course = models.Course.objects.get(id=course_id)

    if not request.user.is_authenticated:
        return False
    elif course.customer.filter(user=request.user).exists():
        return True
    elif course.teacher.filter(user=request.user).exists():
        return True
    return False


@register.simple_tag
def is_discount(course_id):
    course = models.Course.objects.get(id=course_id)
    if course.discount == 0:
        return False

    now = Timezone.now()
    if course.start_discount <= now <= course.end_discount:
        return True

    return False


@register.simple_tag
def time_left_for_discount(course_id):
    course = models.Course.objects.get(id=course_id)

    now = datetime.now(timezone.utc)
    end_discount = course.end_discount.replace(tzinfo=timezone.utc)
    date_difference = end_discount - now

    return format_time(date_difference)


@register.simple_tag
def difference_time_sending_comment(comment_id, is_course_comment=True):
    if is_course_comment:
        comment = models.CourseComment.objects.get(id=comment_id)
    else:
        comment = models.AskedQuestion.objects.get(id=comment_id)

    now = datetime.now(timezone.utc)

    start = comment.created_at.replace(tzinfo=timezone.utc)
    date_difference = now - start
    return format_time(date_difference)


@register.simple_tag
def convert_to_shamsi(string_date):
    date = JalaliDate(string_date)

    return date.strftime('%c', locale='fa')


@register.simple_tag
def number_video_season(id):
    season = models.Season.objects.get(id=id)
    return season.meetings.filter(is_publish=True).exclude(video=None).count()
