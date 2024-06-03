from django.http import JsonResponse

class Response:
    @staticmethod
    def success(message: str):
        return JsonResponse({'success': True, 'message': message})

    @staticmethod
    def error(message: str):
        return JsonResponse({'success': False, 'message': message})
