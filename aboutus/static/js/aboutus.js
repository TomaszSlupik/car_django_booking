document.addEventListener('DOMContentLoaded', function() {
    const accessToken = localStorage.getItem('access'); 

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
})

