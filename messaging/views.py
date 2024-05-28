from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pywhatkit as kit
import json

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone_number = data.get('phone_number')
            message = data.get('message')

            if not phone_number or not message:
                return JsonResponse({'success': False, 'error': 'Phone number and message are required.'})

            # Send WhatsApp message using pywhatkit
            kit.sendwhatmsg_instantly(phone_number, message, 15)
            
            return JsonResponse({'success': True, 'message': 'Message sent successfully.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})
