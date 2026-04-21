# Almaty Tours — Adventure Booking Platform

A full-stack web application for discovering and booking professional mountain tours in Almaty, Kazakhstan. Developed by a local mountain guide and software engineer, this platform combines deep local expertise with a modern tech stack.

## 🚀 Tech Stack

### Frontend
- **Framework:** Angular (v17+)
- **State Management:** Angular Signals
- **Styling:** Custom CSS (Modular)
- **Networking:** HttpClient with Interceptors for JWT handling
- **Routing:** Standalone components with Auth Guards

### Backend
- **Framework:** Django 5.0 + Django REST Framework (DRF)
- **Authentication:** JWT (JSON Web Tokens) via SimpleJWT
- **Database:** PostgreSQL (Robust and production-ready)
- **API Style:** RESTful API

## ✨ Key Features
- **User Authentication:** Secure Login and Registration flow.
- **Tour Discovery:** Explore various mountain tours (Kolsai, Charyn, Shymbulak, etc.).
- **Dynamic Details:** Detailed tour information including pricing, duration, and slots.
- **Booking System:** Interactive booking form with real-time validation.
- **Payment Simulation:** Realistic payment modal with card masking and validation logic.

## 🛠️ Installation & Setup

### 1. Prerequisites
- Node.js & NPM
- Python 3.10+
- PostgreSQL server

### 2. Backend Setup (Django)
1. Navigate to the backend directory.
2. Install dependencies:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary django-cors-headers
