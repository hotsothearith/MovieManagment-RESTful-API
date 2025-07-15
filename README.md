# 🎬 Movie Management RESTful API

This is a **Flask-based RESTful API** for managing a movie database. It allows you to perform CRUD operations on movies, directors, and genres. The API is documented using **Swagger UI**, powered by **Flask-RESTX**, and uses **SQLAlchemy** for ORM-based database management.

---

## 🚀 Features

- ✅ RESTful endpoints for Movies, Genres, and Directors
- 🔁 Full CRUD support
- 🧩 Relational database with SQLAlchemy
- 📄 Interactive Swagger documentation (auto-generated with Flask-RESTX)
- 📦 Modular project structure
- 🔐 Error handling using SQLAlchemy exceptions

---

## 🧰 Tech Stack

- **Backend Framework**: Flask  
- **API Documentation**: Flask-RESTX (Swagger UI)  
- **Database ORM**: SQLAlchemy  
- **Database**: Mysql
- **Python Version**: 3.x

---

## 📂 Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/hotsothearith/MovieManagment-RESTful-API.git
cd MovieManagment-RESTful-API
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
pip install Flask Flask-RESTX Flask-SQLAlchemy

```
4. Run the app
```bash
python app.py
```
