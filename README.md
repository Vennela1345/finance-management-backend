# 💰 Finance Management Backend

A Django REST Framework-based backend system for managing financial records, user authentication, and transaction tracking.

---

## 📌 Overview

This project provides REST APIs for:

* User Management
* Financial Records Management
* Transaction Tracking
* Secure Authentication using JWT

The system follows a modular and scalable architecture.

---

## 🚀 Features

* 🔐 JWT Authentication (Login & Token System)
* 👤 User Management APIs
* 💰 Financial Records CRUD Operations
* 📊 Finance Data Handling
* ✅ Input Validation & Error Handling
* 🗄️ Database Integration

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite (default database)

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/Vennela1345/finance-management-backend.git

cd finance-management-backend

---

### 2. Install Dependencies

pip install -r requirements.txt

---

### 3. Apply Migrations

python manage.py makemigrations
python manage.py migrate

---

### 4. Create Superuser

python manage.py createsuperuser

---

### 5. Run Server

python manage.py runserver

Server will start at:
http://127.0.0.1:8000/

---

## 🔐 Authentication (JWT)

### Get Access Token

**POST** `/api/token/`

#### Request:

{
"username": "your_username",
"password": "your_password"
}

#### Response:

{
"access": "your_access_token",
"refresh": "your_refresh_token"
}

---

## 📡 API Endpoints

### 👤 Users

* GET `/api/users/` → Get all users

---

### 💰 Records

* GET `/api/records/` → Fetch all records
* POST `/api/records/` → Create new record

#### Example Request:

{
"title": "Test Record",
"amount": 100
}

---

### 📊 Finance

* GET `/api/finance/` → Finance summary

---

## 🧪 API Testing

You can test APIs using:

* Postman (collection included in project)
* Swagger UI (if enabled)

---

## ⚠️ Limitations

* Not deployed to cloud
* Basic UI (backend only)
* Limited validation rules

---

## 🔮 Future Improvements

* Deploy to cloud (AWS / Render)
* Add frontend dashboard
* Role-based access control
* Advanced analytics & reports

---

## 👩‍💻 Author
Vennela Gumma


