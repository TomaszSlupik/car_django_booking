const alertRegister = document.getElementById("register-error")
const success = document.getElementById("register-success")

document.addEventListener("DOMContentLoaded", function() {
    if (alertRegister) {
        setTimeout(() => {
            alertRegister.style.display = 'none'
        }, 3000)
    }
})


