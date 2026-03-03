from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# class CustomEmailValidator(RegexValidator):
#     def __init__(self, *args, **kwargs):
#         super().__init__(
#             regex=r'^[a-zA-Z0-9._%+-]+@(university\.com|university\.org)$',
#             message='Email must be from "university.com" or "university.org" domain.',
#             *args, **kwargs
#         )

def validate_email_domain(value):
    allowed_domains = ['university.com', 'university.net', 'university.org']
    if not any(value.endswith(domain) for domain in allowed_domains):
        raise ValidationError(f"Email address is not valid. It must be one of the following: {', '.join(allowed_domains)}")