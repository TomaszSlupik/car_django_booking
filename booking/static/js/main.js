
const reservationButtons = document.querySelectorAll('.btnReservation');

reservationButtons.forEach(function(button) {
    button.addEventListener('click', function (e) {
        e.preventDefault();  
        const bookingId = this.dataset.bookingId;
        console.log("Kliknięty przycisk z booking_id: ", bookingId); 
        const accessToken = localStorage.getItem('access');
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const start_date = document.querySelector('#start_date').value
        const end_date = document.querySelector('#end_date').value

        console.log(accessToken)
        if (!accessToken) {
            console.error("Brak tokenu dostępu. Użytkownik może nie być zalogowany.");
            Swal.fire(
                'Błąd',
                'Musisz być zalogowany, aby zarezerwować.',
                'error'
            );
            return;  
        }

        Swal.fire({
            title: 'Czy chcesz zarezerwować?',
            text: "Potwierdź, jeśli jesteś pewien.",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Akceptuję',
            cancelButtonText: 'Anuluj',
            reverseButtons: true
        })
        .then((result) => {
            if (result.isConfirmed) {
                fetch('main/booking/',  {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${accessToken}`,  
                        'X-CSRFToken': csrfToken 
                    },
                    body: JSON.stringify({
                        booking_id: bookingId,
                        start_date: start_date,
                        end_date: end_date
                    })
                }).then(response => response.json())  
                .then(data => {
                    console.log("Odpowiedź serwera:", data);  
                    if (data.status === 'success') {
                        Swal.fire(
                            'Zarezerwowane!',
                            'Twoja rezerwacja została potwierdzona.',
                            'success'
                        );
                        button.disabled = true;
                        button.textContent = 'ZAREZERWOWANE';
                        button.closest('.card').classList.add('booked');
                    } else {
                        Swal.fire(
                            'Błąd',
                            data.message,
                            'error'
                        );
                    }
                })
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                Swal.fire(
                    'Anulowane',
                    'Twoja rezerwacja została anulowana.',
                    'error'
                );
            }
        });
    });
});