# LittleLemon
This is a back-end application for a restaurant website using Django framework.

# URLs

* home:        http://localhost:8000/
* about:       http://localhost:8000/about/
* book:        http://localhost:8000/book/
* refresh bookings when you select a reservation date in the book page
  * http://localhost:8000/bookings/?date=2023-01-01
* reservations: http://localhost:8000/reservations/
* login:        http://localhost:8000/auth/token/login
* logout:       http://localhost:8000/auth/token/logout
* POST http://localhost:8000/book/
    * headers: "Content-type":"application/json"
    * submitting a reservation to server