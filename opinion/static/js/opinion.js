document.addEventListener('DOMContentLoaded', function() {
    const opinionForm = document.getElementById('opinion-form'); 
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; 
    const accessToken = localStorage.getItem('access'); 

    // Sprawdzanie, czy użytkownik jest zalogowany 
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


    // Formularz opini 
    opinionForm.addEventListener('submit', function(event) {
        event.preventDefault(); 

        // Ustawienie flagi zeby 2x nie wysyłać
        if (opinionForm.dataset.submitted === 'true') {
            return; 
        }
        opinionForm.dataset.submitted = 'true';

      

        const booking = document.querySelector('[name="booking"]').value; 
        const rating = document.querySelector('[name="rating"]:checked').value; 
        const comment = document.querySelector('[name="comment"]').value; 

        const dataToSend = {
            booking: booking,
            rating: rating,
            comment: comment
        };

        // Wysyłka
        fetch(opinionForm.action, { 
            method: 'POST',
            body: JSON.stringify(dataToSend), 
            headers: {
                'Content-Type': 'application/json', 
                'X-CSRFToken': csrfToken, 
                'Authorization': `Bearer ${accessToken}` 
            }
        })
        .then(response => response.json())  
        .then(data => {
            if (data.success) {
                Swal.fire({
                    title: 'Sukces!',
                    text: data.message,
                    icon: 'success',
                    confirmButtonText: 'OK'
                }).then(() => {
                    opinionForm.reset();  
                });
            } else {
                Swal.fire({
                    title: 'Błąd!',
                    text: data.message || 'Wystąpił błąd podczas dodawania opinii. Spróbuj ponownie.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        })
        .catch(error => {
            Swal.fire({
                title: 'Błąd!',
                text: 'Wystąpił problem z połączeniem. Spróbuj ponownie.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        })
        .finally(() => {
            // Przywracam flagę
            opinionForm.dataset.submitted = 'false'; 
        });
    });
});
