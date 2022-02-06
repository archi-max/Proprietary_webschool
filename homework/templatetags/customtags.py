
from homework.models import Work, Submission
# Create your views here.
from django import template
register = template.Library()

def get_submission_file(work, user):
    submission = Submission.objects.filter(work=work, user=user)
    if submission:
        return submission[0].file
    else:
        return None

@register.filter
def submission_file(work, user):
    return get_submission_file(work, user)

