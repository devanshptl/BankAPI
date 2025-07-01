#  Indian Banks REST API

A Django-based REST API that provides detailed data on Indian banks and their branches across the country.


---

##  Features

- List all banks
- Fetch branch details using IFSC
- Filter branches by bank name and city
- Bulk CSV data loader from official RBI dataset
- Designed with Django REST Framework

---

## 🛠 Tech Stack

- **Backend**: Django + Django REST Framework
- **Database**: SQLite
- **Testing**: Django’s built-in `TestCase`

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/devanshptl/BankAPI.git
cd bankapi
```

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run migrations and load data

```bash
python manage.py migrate
python manage.py load_data
```

Make sure `bank_branches.csv` is in `core/data/`.

### 4. Run the server

```bash
python manage.py runserver
```

---

##  Running Tests

```bash
python manage.py test
```

---

## API Endpoints

| Method | Endpoint                         | Description                         |
|--------|----------------------------------|-------------------------------------|
| GET    | `/banks/`                        | List all banks                      |
| GET    | `/branches/<ifsc>/`              | Get branch by IFSC code             |
| GET    | `/branches/?bank_name=X&city=Y`  | Filter branches by bank & city      |

---

## Project Structure

```
bankapi/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── management/commands/load_data.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---



