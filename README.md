# ProductFlow API

A RESTful **Product & Order Management API** built with **FastAPI** and **SQLAlchemy**.

The project provides product CRUD operations, inventory quantity management, order creation, and automated API testing.

## Features

* Product CRUD operations
* Increase and decrease product inventory
* Stock validation
* Order creation and management
* Product availability validation during order creation
* SQLite database by default
* Support for MySQL and PostgreSQL
* Pydantic request/response validation
* Service and repository layer architecture
* Automated tests with Pytest
* FastAPI automatic Swagger documentation

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite / MySQL / PostgreSQL
* Uvicorn
* Pytest

## Project Structure

```text
ProductFlow-API/
│
├── app/
│   ├── api/
│   │   └── products.py
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   ├── models/
│   │   └── product.py
│   │
│   ├── repository/
│   │   └── product_repository.py
│   │
│   ├── schemas/
│   │   └── product.py
│   │
│   ├── services/
│   │   └── product_services.py
│   │
│   ├── orders/
│   │   ├── api/
│   │   ├── interfaces/
│   │   ├── models/
│   │   ├── repository/
│   │   ├── schemas/
│   │   └── services/
│   │
│   └── main.py
│
├── tests/
│   └── test_produce.py
│
├── .env.example
├── requirements.txt
└── products.db
```

## Installation

Clone the repository:

```bash
git clone https://github.com/KshamaDaddi/ProductFlow-API.git
cd ProductFlow-API
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Configuration

The project uses SQLite by default:

```env
DATABASE_URL=sqlite:///./products.db
```

You can also configure MySQL:

```env
DATABASE_URL=mysql+pymysql://USERNAME:PASSWORD@localhost/DATABASE_NAME
```

Or PostgreSQL:

```env
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@localhost/DATABASE_NAME
```

Create a `.env` file in the project root if you want to configure the database.

## Run the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Health

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | `/`       | Check API status |
| GET    | `/health` | Health check     |

### Products

| Method | Endpoint                                   | Description       |
| ------ | ------------------------------------------ | ----------------- |
| POST   | `/products/`                               | Create a product  |
| GET    | `/products/`                               | Get all products  |
| GET    | `/products/{product_id}`                   | Get product by ID |
| PUT    | `/products/{product_id}`                   | Update product    |
| DELETE | `/products/{product_id}`                   | Delete product    |
| PATCH  | `/products/{product_id}/quantity`          | Reduce stock      |
| PATCH  | `/products/{product_id}/quantity/increase` | Increase stock    |

### Orders

| Method | Endpoint             | Description     |
| ------ | -------------------- | --------------- |
| POST   | `/orders/`           | Create an order |
| GET    | `/orders/`           | Get all orders  |
| GET    | `/orders/{order_id}` | Get order by ID |
| DELETE | `/orders/{order_id}` | Delete an order |

## Example: Create Product

```http
POST /products/
```

Request:

```json
{
  "name": "Laptop",
  "description": "Developer laptop",
  "price": 50000,
  "quantity": 10
}
```

## Example: Create Order

```http
POST /orders/
```

Request:

```json
{
  "product_id": 1,
  "quantity": 2
}
```

When an order is created, the API checks product availability and reduces the corresponding inventory quantity.

## Testing

Run the complete test suite:

```bash
python -m pytest
```

The tests cover:

* Product creation
* Product retrieval
* Product update
* Product deletion
* Product-not-found handling
* Inventory reduction
* Insufficient-stock validation
* Inventory increase
* Order creation

## Architecture

The application follows a layered architecture:

```text
Client
  │
  ▼
FastAPI Routes
  │
  ▼
Service Layer
  │
  ▼
Repository Layer
  │
  ▼
SQLAlchemy
  │
  ▼
Database
```

This separation keeps API routes, business logic, and database operations independent and easier to maintain.

## Error Handling

The API returns appropriate HTTP errors for common invalid operations, including:

* `400 Bad Request` — invalid operation or insufficient inventory
* `404 Not Found` — product or order does not exist

## Author

**Kshama Daddi**

GitHub: [KshamaDaddi](https://github.com/KshamaDaddi)

---

## License

This project is intended for learning, development, and portfolio purposes.
