# ✈ Travel Booking App

A simple Django-based travel booking application where users can browse trips, book seats, and manage their bookings.  
Built with **Django**, **Bootstrap 5**, and deployed on **Render**.

---

## 🚀 Features
- User authentication (Login / Signup / Logout)
- Browse available trips
- Book seats in real-time
- View and manage personal bookings
- Responsive UI with Bootstrap

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (local), PostgreSQL (on Render)
- **Deployment:** Render Cloud

---

## 📂 Project Structure

```bash
travel_booking/                 # Root project folder
├── accounts/                   # Django app for authentication
│   ├── migrations/             
│   ├── templates/accounts/     
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── forms.py
│
├── travel/                     # Django app for travels/bookings
│   ├── migrations/
│   ├── templates/travel/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── forms.py
│
├── travel_booking/             # Project settings & configs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/                     # Static files (css, js, images)
│   ├── css/style.css
│   └── js/script.js
│
├── templates/                  # Shared templates
│   ├── base.html
│   └── partials/_messages.html
│
├── .gitignore
├── manage.py
├── Procfile
├── requirements.txt
├── runtime.txt
└── README.md
