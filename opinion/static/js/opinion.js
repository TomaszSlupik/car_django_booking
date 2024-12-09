document.addEventListener('DOMContentLoaded', function() {
    const opinionForm = document.getElementById('opinion-form'); // Formularz opinii
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Pobieranie CSRF tokenu
    const accessToken = localStorage.getItem('access'); // Pobieranie tokenu dostępu

    // Sprawdzanie, czy użytkownik jest zalogowany (czy access token istnieje)
    if (!accessToken) {
        console.error("Brak tokenu dostępu. Użytkownik może nie być zalogowany.");
        Swal.fire({
            title: 'Błąd!',
            text: 'Musisz być zalogowany, aby korzystać z aplikacji',
            icon: 'error',
            confirmButtonText: 'OK'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = 'http://127.0.0.1:8000/';
            }
        });
        return;  
    }


    // Obsługuje wysyłanie formularza opinii
    opinionForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Zatrzymujemy normalne wysyłanie formularza

      
        // Pobieranie wartości z formularza
        const booking = document.querySelector('[name="booking"]').value; // Samochód (ID rezerwacji)
        const rating = document.querySelector('[name="rating"]:checked').value; // Ocena (wartość wybranego radia)
        const comment = document.querySelector('[name="comment"]').value; // Komentarz

        // Tworzymy obiekt z danymi do wysłania
        const dataToSend = {
            booking: booking,
            rating: rating,
            comment: comment
        };

        // Wyślij formularz za pomocą fetch
        fetch(opinionForm.action, { // URL formularza
            method: 'POST',
            body: JSON.stringify(dataToSend), // Wysyłamy dane formularza w formacie JSON
            headers: {
                'Content-Type': 'application/json', // Określamy, że wysyłamy dane w formacie JSON
                'X-CSRFToken': csrfToken, // Dodajemy CSRF token w nagłówkach
                'Authorization': `Bearer ${accessToken}` // Dodajemy access token w nagłówkach
            }
        })
        .then(response => response.json())  // Oczekujemy odpowiedzi w formacie JSON
        .then(data => {
            // Obsługa odpowiedzi serwera
            if (data.success) {
                // Jeśli wysłano opinię pomyślnie
                Swal.fire({
                    title: 'Sukces!',
                    text: data.message,
                    icon: 'success',
                    confirmButtonText: 'OK'
                }).then(() => {
                    opinionForm.reset();  // Resetowanie formularza po dodaniu opinii
                });
            } else {
                // Jeśli wystąpił błąd
                Swal.fire({
                    title: 'Błąd!',
                    text: data.message || 'Wystąpił błąd podczas dodawania opinii. Spróbuj ponownie.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        })
        .catch(error => {
            // Obsługuje błąd połączenia
            Swal.fire({
                title: 'Błąd!',
                text: 'Wystąpił problem z połączeniem. Spróbuj ponownie.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        });
    });
});
