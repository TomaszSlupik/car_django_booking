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
            window.location.href = '/main/';
        } else {
            const error = await res.json();
            alert (error.error)
            console.log('Logowanie nie powiodło się');
        }
    } catch (error) {
        console.log('Błąd:', error); 
    }
}


