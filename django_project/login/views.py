from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_index(request):
    return HttpResponse("""
    <html>
        <body>
            Login Here
            <form action="/check_email/" method="post">
                {% csrf_token %}
                <label for="check_email">Your Email: </label>
                <input id="check_email" type="text" name="check_email" value="">
                <input type="submit" value="OK">
            </form>
        </body>
    </html>
    """)

# Check email against database
def check_email(request):
    return HttpResponse("""Email Checked""")
