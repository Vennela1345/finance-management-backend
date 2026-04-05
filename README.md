# Finance-Management-Backend
A Django REST Framework-based backend system for managing finance records, user authentication, and transaction tracking. The project provides APIs for handling finance data efficiently with proper modular architecture. 

# 🚀 Django Backend API Project

## 📌 Overview

This is a Django REST API project with:

* User Management
* Records Management
* Finance Module
* JWT Authentication

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/Vennela1345/finance-management-backend.git
cd backend-project

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run Migrations

python manage.py makemigrations
python manage.py migrate

### 4. Create Superuser

python manage.py createsuperuser

### 5. Run Server

python manage.py runserver

---

## 🔐 Authentication (JWT)

### Get Token

POST /api/token/

Request:
{
"username": "vennela",
"email": "gummavennela@gmail.com"
"password": "venni"
}

Response:
{
"access": "your_access_token",
"refresh": "your_refresh_token"
}

---

## 📡 API Endpoints

### Users

GET /api/users/

### Records

GET /api/records/
POST /api/records/

Example POST:
{
"title": "Test Record",
"amount": 100
}

### Finance

GET /api/finance/

---

## 🧪 API Testing

Use Postman collection included:
postman_collection.json

---

## 👨‍💻 Author
Vennela Gumma

Vennela Gumma

