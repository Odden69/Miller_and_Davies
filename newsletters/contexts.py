from django.contrib import messages
from .models import NewsletterSubscriber
from .forms import NewsletterSignupForm


def newsletter_signup(request):
    """
    Makes the newsletter sign up form available throughout the site
    """

    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterSubscriber.objects.filter(
             email=instance.email).exists():
                form = NewsletterSignupForm()
                messages.info(request, 'You are already a subscriber. \
                Please check your spam inbox for emails.')
            else:
                instance.save()
                form = NewsletterSignupForm()
                messages.success(request, 'Thank you for \
                    subscribing for our newsletters!')

    else:
        form = NewsletterSignupForm()

    context = {
        'newsletter_signup_form': form,
    }

    return context
