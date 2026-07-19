# 🎓 School Management System API

A robust **School Management System REST API** built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**. This project provides secure and scalable APIs for managing students, teachers, classes, attendance, exams, subjects, fees, announcements, and user authentication.

---

##  Features

-  JWT Authentication & Authorization
-  User Registration & Login
-  Student Management
-  Teacher Management
-  School Class Management
-  Subject Management
-  Exam Management
-  Attendance Management
-  Fee Management
-  Announcement Management
-  Interactive Swagger Documentation
-  PostgreSQL Database
-  Alembic Database Migrations
-  Modular Project Structure

---

## 🛠 Tech Stack

| Technology | Description |
|------------|-------------|
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database Migration |
| JWT | Authentication |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
| Passlib & Bcrypt | Password Hashing |

---

# 📂 Project Structure

```
School-Management-System-API
│
├── alembic/
├── app/
│   ├── api/
│   ├── controller/
│   ├── db/
│   ├── models/
│   ├── schema/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
├── alembic.ini
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/School-Management-System-API.git

cd School-Management-System-API
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a **.env** file.

```env
DATABASE_URL=postgresql://username:password@localhost:5432/school_management

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run Database Migration

```bash
alembic upgrade head
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔐 Authentication

- Register User
- Login User
- Password Hashing using Bcrypt
- JWT Token Generation
- Protected Routes

---

# 📌 Modules

✔ Authentication

✔ Students

✔ Teachers

✔ School Classes

✔ Subjects

✔ Attendance

✔ Exams

✔ Fees

✔ Announcements

---

# 📸 Swagger UI

## Home

![Swagger Home](images/swagger-home.png)

---

## Authentication

![Authentication](images/authentication.png)

---

## Student APIs

![Students](images/student-api.png)

---

## Teacher APIs

![Teachers](images/teacher-api.png)

---

## School Class APIs

![Classes](images/class-api.png)

---

## Subject APIs

![Subjects](images/subject-api.png)

---

## Attendance APIs

![Attendance](images/attendance-api.png)

---

## Exam APIs

![Exams](images/exam-api.png)

---

## Fee APIs

![Fees](images/fee-api.png)

---

## Announcement APIs

![Announcements](images/announcement-api.png)

---
## Authorization User

![Authorization](images/authorization.png)

## Authorized User

![Authorized](images/authorize.png)

---

# 🗃 Database

PostgreSQL is used as the primary database.

Database migrations are managed using Alembic.

---

# 🔒 Security

- JWT Authentication
- Password Hashing
- Protected APIs
- Request Validation
- SQLAlchemy ORM

---

# 🚀 Future Improvements

- Role Based Access Control
- Refresh Token
- Email Verification
- Password Reset
- File Upload
- Dashboard Analytics
- Docker Support
- CI/CD Pipeline
- Unit Testing

---

# 👨‍💻 Author

**pratik patidar **

GitHub:
 https://github.com/pratikdevbuilds

LinkedIn:
https://www.linkedin.com/in/pratik-patidar-64557a328/

---

# ⭐ Support

If you found this project helpful, don't forget to give it a ⭐ on GitHub.
