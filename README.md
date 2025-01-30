### 1. Technologie

Aplikacja została zbudowana z wykorzystaniem następujących technologii:
- **Django** – wykorzystywany do tworzenia backendu aplikacji, obsługujący logikę biznesową, autentykację, rezerwację samochodów oraz interakcję z bazą danych.
- **Sqlite3** – domyślnie użyto bazę, która przychodzi z Django, służąca do przechowywania informacji o rezerwacjach użytkownikach.
- **Bootstrap** – framework CSS, który został użyty do szybkiego prototypowania oraz tworzenia responsywnych interfejsów użytkownika.

## Wykorzystane technologie i narzędzia

[![My Skills](https://skillicons.dev/icons?i=html,scss,bootstrap,sqlite,django,git,vscode,postman)](https://skillicons.dev)



<!-- globalbe -->
sass --watch main/static/main.scss:main/static/main.css --load-path=car_django/static
sass --watch users/static/login.scss:users/static/login.css --load-path=car_django/static
sass --watch booking/static/booking.scss:booking/static/booking.css --load-path=car_django/static

sass --watch car_django/static/index.scss:car_django/static/index.css --load-path=car_django/static
sass --watch contact/static/contact.scss:contact/static/contact.css --load-path=car_django/static
sass --watch aboutus/static/aboutus.scss:aboutus/static/aboutus.css --load-path=car_django/static
sass --watch opinion/static/opinion.scss:opinion/static/opinion.css --load-path=car_django/static

# $ python manage.py test booking.test.test_booking