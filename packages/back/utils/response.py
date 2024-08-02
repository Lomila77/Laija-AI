from django.http import JsonResponse

class Response:
    @staticmethod
    def success(message: str):
        return JsonResponse({'success': True, 'message': message}, status=200)

    @staticmethod
    def error(message: str):
        return JsonResponse({'success': False, 'message': message}, status=500)
