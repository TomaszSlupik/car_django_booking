(() => {
    'use strict'
    const forms = document.querySelectorAll('.needs-validation')
  
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        event.preventDefault(); 
        if (form.checkValidity()) {
          Swal.fire({
            title: 'Twoja wiadomość została wysłana',
            text: "Wszystko przebiegło pomyślnie",
            icon: 'success',
            confirmButtonText: 'Akceptuję',
            reverseButtons: true
          })
        }
        else {
          event.stopPropagation()
          event.preventDefault(); 
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()

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


