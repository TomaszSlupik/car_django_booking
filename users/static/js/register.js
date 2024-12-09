const alert = document.getElementById("register-error")
const success = document.getElementById("register-success")

document.addEventListener("DOMContentLoaded", function() {
    if (alert) {
        setTimeout(() => {
            alert.style.display = 'none'
        }, 3000)
    }
})


