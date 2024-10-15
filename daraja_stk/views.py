from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
# views.py

def mpesa_callback(request):
    if request.method == 'POST':
        # Here you can handle the incoming data from M-Pesa
        callback_data = request.body
        print("Callback data received: ", callback_data)

        # Process the callback data and respond
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
    return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid request"}, status=400)
