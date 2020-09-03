from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView,CreateView,FormView
from .models import Membership, UserMembership, Subscription
from .forms import SignUpForm,ContactForm

class MembershipView(ListView):
    model = Membership
    template_name = 'omember/list.html'    
    
    def get_user_membership(self,request):
        user_membership_qs = UserMembership.objects.filter(user=self.request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first()
        return None    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = self.get_user_membership(self.request)
        context['current_membership'] = str(current_membership)
        return context

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'omember/create.html'
    # must be lazy loading because urls are not loaded yet, otherwise crash!
    success_url = reverse_lazy('membership:index')

    def form_valid(self, form):
        #print(type(model))
        return super().form_valid(form)


class ContactView(FormView):
    template_name = 'omember/landing.html'
    form_class = ContactForm
    success_url = reverse_lazy('membership:index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

def index(request):
    return render(request,'omember/index.html')