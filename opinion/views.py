from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OpinionForm
from django.http import JsonResponse
from .models import Opinion
import json
from booking.models import Booking
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

# Create your views here.
def opinion_view(request):
    # pusty formularz
    form = OpinionForm()  

    opinions = Opinion.objects.all().select_related("booking", "user")
    return render(request, 'opinion.html', {'form': form, 'opinions': opinions})


def add_opinion(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body)
            booking_id = data.get('booking')  # ID rezerwacji
            rating = data.get('rating')  # Ocena
            comment = data.get('comment')  # Komentarz
            access_token = request.headers.get('Authorization') 

            print(f"Dane: booking_id={booking_id}, rating={rating}, comment={comment}")
            
            if not access_token:
                return JsonResponse({
                    'success': False,
                    'message': 'Musisz być zalogowany, aby dodać opinię.'
                })

            access_token = access_token.split(' ')[1]

            # Weryfikacja tokenu
            try:
                token = AccessToken(access_token)
                user_id = token['user_id']  
                user = User.objects.get(id=user_id)  
            except Exception as e:
                print(f"Błąd podczas weryfikacji tokenu: {str(e)}")
                return JsonResponse({
                    'success': False,
                    'message': 'Niepoprawny token, użytkownik nie jest zalogowany.'
                })

            # czy wszystkie dane zostały przekazane
            if not all([booking_id, rating, comment]):
                return JsonResponse({
                    'success': False,
                    'message': 'Wszystkie pola są wymagane.'
                })

            # Sprawdzam, czy rezerwacja z takim booking_id istnieje
            try:
                booking = Booking.objects.get(id=booking_id)
            except Booking.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'Nie znaleziono rezerwacji o podanym ID.'
                })

            # Sprawdzam, czy użytkownik już dodał opinię do tej rezerwacji
            if Opinion.objects.filter(booking=booking, user=user).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Już dodałeś opinię do tej rezerwacji.'
                })

            # Formularz z danymi
            form = OpinionForm({
                'booking': booking,
                'rating': rating,
                'comment': comment
            })

            # Sprawdzam, czy formularz jest prawidłowy
            if form.is_valid():
                opinion = form.save(commit=False)
                opinion.user = user 
                opinion.save()  
                print(f"Opinia zapisana: {opinion}")

                return JsonResponse({
                    'success': True,
                    'message': 'Opinia została dodana pomyślnie!'
                })

            else:
                errors = form.errors.as_json()  
                print(f"Błędy formularza: {errors}")
                return JsonResponse({
                    'success': False,
                    'message': 'Formularz zawiera błędy.',
                    'errors': errors
                })

        except json.JSONDecodeError:
            print(f"Błędny format danych: {request.body}")
            return JsonResponse({
                'success': False,
                'message': 'Błędny format danych.'
            })

        except Exception as e:
            print(f"Błąd: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': f'Wystąpił błąd: {str(e)}'
            })

    # Jeśli metoda HTTP to nie POST
    return JsonResponse({
        'success': False,
        'message': 'Błąd połączenia.'
    })