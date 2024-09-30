
const reservationButtons = document.querySelectorAll('.btnReservation');

reservationButtons.forEach(function(button) {
    button.addEventListener('click', function (e) {
        e.preventDefault();  

        Swal.fire({
            title: 'Czy chcesz zarezerwować?',
            text: "Potwierdź, jeśli jesteś pewien.",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Akceptuję',
            cancelButtonText: 'Anuluj',
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire(
                    'Zarezerwowane!',
                    'Twoja rezerwacja została potwierdzona.',
                    'success'
                );
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
