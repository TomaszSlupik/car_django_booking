(() => {
    'use strict'
    const forms = document.querySelectorAll('.needs-validation')
  
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()


const exampleModal = document.getElementById('exampleModal');
const svgIcon = document.querySelector('.bi-info-circle-fill'); // SVG, który uruchamia modal
const acceptButton = document.querySelector('.acceptButton');


if (exampleModal) {
  svgIcon.addEventListener('click', () => {
    const modal = new bootstrap.Modal(exampleModal);
    modal.show();
  });
}

// Dodałem do usuwania z DOM wszytskich klas modal-backdrop
function removeModalBackdrops() {
  const backdrops = document.querySelectorAll('.modal-backdrop');
  backdrops.forEach(backdrop => {
    backdrop.remove(); 
  });
}

acceptButton.addEventListener('click', () => {
  const modal = bootstrap.Modal.getInstance(document.getElementById('exampleModal'));
  modal.hide(); 
  removeModalBackdrops();
});



async function checkLoginUser(e) {
    e.preventDefault();
    const formData = new FormData(document.getElementById('login-form')); 
    const data = Object.fromEntries(formData); 

    try {
        const res = await fetch('/', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data), 
        });

        if (res.ok) {
            const tokens = await res.json(); 
            localStorage.setItem('refresh', tokens.refresh);
            localStorage.setItem('access', tokens.access);
            localStorage.setItem('username', tokens.username); 
            window.location.href = '/main/';
        } else {
            const error = await res.json();
            const alertDiv = document.getElementById('login-error');
            const alertMessage = document.getElementById('alert-message');

            alertMessage.textContent = error.error; 
            alertDiv.classList.remove('d-none'); 
            
            setTimeout(() => {
                alertDiv.classList.add('d-none'); 
            }, 3000);
        
        }
    } catch (error) {
        console.log('Błąd:', error); 
        
    }
}


