from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def show_messages(request):
    # Add different types of messages
    messages.debug(request, 'This is a debug message.')
    messages.info(request, 'This is an info message.')
    messages.success(request, 'This is a success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')

    return render(request, 'msg/show_messages.html')