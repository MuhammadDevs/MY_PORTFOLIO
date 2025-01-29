from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        user_email = request.POST.get('email', '')  # User's email address
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Prepare email content
        email_subject = f"Contact Form Submission: {subject}"
        email_body = f"""
        You have received a new message from your contact form:

        Name: {name}
        Email: {user_email}
        Subject: {subject}
        
        Message:
        {message}
        """

        try:
            # Send the email
            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=user_email,  # Your app's Gmail account
                to=['mawais221114@gmail.com'],      # Recipient's email (your email)
                reply_to=[user_email],              # Set reply-to as user's email
            )
            email.send()

            # Success message
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            # Error message
            messages.error(request, f"An error occurred: {e}")

        # Redirect to the contact page with query string
        return redirect('/contact?submitted=true')

    return render(request, 'contact.html')