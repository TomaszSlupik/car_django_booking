function clearLocalStorage() {
    localStorage.clear();  
    console.log("LocalStorage został wyczyszczony.");
}

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


// Rezerwacje użytkowników
document.addEventListener('DOMContentLoaded', function () {
    let username = localStorage.getItem('username');  
    console.log(username);

    if (username) {

        let usernameLink = document.getElementById('username');
        
        usernameLink.addEventListener('click', function(event) {
            event.preventDefault();  
            window.location.href = `/main/booking/user/?username=${username}`;
        });
    } else {
        document.getElementById('user-rezerwacje').innerHTML = "<p>Nie znaleziono użytkownika w localStorage.</p>";
    }
});
