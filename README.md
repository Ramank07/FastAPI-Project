# 📝 FastAPI User Post Management API

A simple and modular RESTful API built with **FastAPI** for managing user posts. The application supports full CRUD operations, uses **PostgreSQL** for storage, and **SQLAlchemy** ORM for database interaction. Pydantic models are used for request validation and structured responses.

---

## 🚀 Features

- ✅ Get all user posts
- 📧 Retrieve posts by email
- ➕ Create new post
- 🔁 Update existing post by ID
- ❌ Delete post by ID
- 🧾 Input validation via Pydantic
- 🧱 PostgreSQL + SQLAlchemy integration
- 🔀 Modular structure using APIRouter

---

## 📦 Tech Stack

- **FastAPI** – High-performance API framework
- **SQLAlchemy** – Python ORM
- **PostgreSQL** – Relational database
- **Pydantic** – Data validation and parsing
- **Uvicorn** – ASGI server
- **Git** – Version control

---

## 📁 Project Structure

FastApiAssignment/
├── app/
│ ├── main.py # App entry point
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # DB connection and session
│ └── routers/
│ └── userRoutes.py # User post routes
├── venv/ # Virtual environment
├── .gitignore
└── README.md

pgsql
Copy
Edit

---

## ⚙️ API Endpoints

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/user/post/`         | Get all user posts                   |
| POST   | `/user/post/`         | Create a new user post               |
| GET    | `/user/post/{email}`  | Get posts by user email              |
| PUT    | `/user/post/{id}`     | Update post by ID                    |
| DELETE | `/user/post/{id}`     | Delete post by ID                    |

---

## 📌 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FastApiAssignment.git
cd FastApiAssignment
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Unix/Mac:
source venv/bin/activate
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Server
bash
Copy
Edit
uvicorn app.main:app --reload
Access API docs at:
👉 http://127.0.0.1:8000/docs

🛡️ .gitignore Best Practices
Ensure .gitignore includes:

gitignore
Copy
Edit
venv/
__pycache__/
.env
*.log
*.sqlite3
🧠 Future Improvements
✅ JWT Authentication

📄 Pagination and filtering

🐳 Docker support

🧪 Unit tests with pytest

👨‍💻 Author
Raman Kumar

