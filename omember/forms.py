from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Membership, UserMembership, Subscription
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    free_membership = Membership.objects.get(membership_type='Free')    

    class Meta(UserCreationForm.Meta):
        model = User    
        
    def save(self):
        user = super().save(commit=False)
        user.save()      # Creating a new UserMembership
        user_membership = UserMembership.objects.create(user=user, membership=self.free_membership)
        user_membership.save()      # Creating a new UserSubscription
        user_subscription = Subscription()
        user_subscription.user_membership = user_membership
        user_subscription.save()
        return user


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    error_css_class = 'error'
    required_css_class = 'bold'

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
