// usuwanie rezerwacji:
window.onload = function() {
    const reservationButtons = document.querySelectorAll('.deleteBookingIcon'); 
    reservationButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const bookingId = this.dataset.bookingId;  
            const accessToken = localStorage.getItem('access');
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            
            Swal.fire({
                title: 'Czy chcesz zwolnić tę rezerwację?',
                text: "Ta akcja zwolni rezerwację",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Tak, zwolnij!',
                cancelButtonText: 'Anuluj',
                reverseButtons: true
            }).then((result) => {
                if (result.isConfirmed) {
                    // Jeśli użytkownik potwierdzi, wysyłamy żądanie do backendu
                    fetch(`/main/delete/${bookingId}/`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${accessToken}`,
                            'X-CSRFToken': csrfToken
                        },
                    })
                    .then(response => {
                        console.log(response);
                        return response.json(); 
                    })
                    .then(data => {
                        console.log(data);
                        if (data.status === 'success') {
                            Swal.fire(
                                'Zwolniono!',
                                'Wystąpił problem podczas zwalniania rezerwacji.',
                                'success'
                            );
                            // Usuwamy rezerwację z tabeli na stronie
                            button.closest('tr').remove();
                        } else {
                            Swal.fire(
                                'Błąd',
                                'Wystąpił błąd podczas zwalniania rezerwacji.',
                                'error'
                            );
                        }
                    })
                    .catch(error => {
                        console.error('Błąd przy zwalnianiu:', error);
                        Swal.fire(
                            'Błąd',
                            'Wystąpił błąd podczas zwalniania rezerwacji.',
                            'error'
                        );
                    });
                } else if (result.dismiss === Swal.DismissReason.cancel) {
                    Swal.fire(
                        'Anulowane',
                        'Twoja rezerwacja nie została zwolniona.',
                        'info'
                    );
                }
            });
        });
    });
};