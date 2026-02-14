from django import template

register = template.Library()

@register.inclusion_tag('common/user_info.html', takes_context=True)
def user_info(context):
    print(context)
    if context['user'].is_authenticated:
        return {
            'username': context['user'].username,

        }
    return {
        'username': "Anonymous",
    }
