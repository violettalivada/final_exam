from django import template

register = template.Library()


@register.filter
def page_query_string(request, page_number):
    query_args = request.GET.copy()
    query_args['page'] = page_number
    return query_args.urlencode()


@register.simple_tag
def get_companion(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None