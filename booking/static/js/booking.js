const reservationButtons = document.querySelectorAll('.btnReservation');
const resert_filter = document.querySelector('.reset_filter')


// Resetowanie filtra:
const resetAllCar= () => {
    console.log("Reset")
    window.location.href = window.location.pathname;
}

resert_filter.addEventListener("click", resetAllCar)


document.addEventListener('DOMContentLoaded', function() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');

    const formattedDate = `${year}-${month}-${day}`;

    // Jeżeli puste ustawiam na dzisiejszą datę
    document.querySelectorAll('[id^="start_date_reservation"]').forEach(function(input) {
        if (!input.value) {
            input.value = formattedDate;
        }
    });
    document.querySelectorAll('[id^="end_date_reservation"]').forEach(function(input) {
        if (!input.value) {
            input.value = formattedDate;
        }
    });
});


reservationButtons.forEach(function(button) {
    button.addEventListener('click', function (e) {
        e.preventDefault();  
        const bookingId = this.dataset.bookingId;
        console.log("Kliknięty przycisk z booking_id: ", bookingId); 
        const accessToken = localStorage.getItem('access');
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const start_date = document.querySelector(`#start_date_reservation_${bookingId}`).value;
        const end_date = document.querySelector(`#end_date_reservation_${bookingId}`).value;

        const username = localStorage.getItem('username'); 
        console.log("Start date:", start_date);
        console.log("End date:", end_date);

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

        if (!start_date || !end_date) {
            console.error("Start date i end date są puste");
            Swal.fire(
                'Błąd',
                'Proszę wybrać daty rozpoczęcia i zakończenia.',
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
                        end_date: end_date, 
                        username: username
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


document.addEventListener('DOMContentLoaded', function() {
    const carNameInput = document.getElementById('car_name_input');

    carNameInput.addEventListener('input', function() {
        const carName = carNameInput.value.trim();

        const url = new URL(window.location.href);
        
        // Dodaje car_name do url lub usuwam
        if (carName) {
            url.searchParams.set('car_name', carName);  
            url.searchParams.delete('car_name');  
        }
    });
});


