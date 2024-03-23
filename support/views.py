from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def about_view(request):
    return render(request, 'support/about.html') 

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            messages.success(request, 'Your message has been sent! We will be in touch shortly.')
            # Adjusted to use the namespaced URL
            return redirect('support:contact')  # Redirect using the 'support' namespace
    else:
        form = ContactForm()

    return render(request, 'support/contact.html', {'form': form})