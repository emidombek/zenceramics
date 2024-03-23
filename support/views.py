from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def about_view(request):
    return render(request, 'support/about.html') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            messages.success(request, 'Your message has been sent!')
            return redirect('contact')  # Redirect to a new URL
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'support/contact.html', {'form': form})