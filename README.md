# MITBrandsAPI
The API is running at http://localhost:8000

## Usage
API Endpoints

### Products:

GET /api/products/: Get a list of products.
GET /api/products/{id}/: Get details of a specific product.
POST /api/products/: Add a new product (admin only).
PUT /api/products/{id}/: Update product details (admin only).
DELETE /api/products/{id}/: Remove a product (admin only).

### Orders:

GET /api/orders/: Get a list of orders.
GET /api/orders/{id}/: Get details of a specific order.
POST /api/orders/: Place a new order.

### Users:

POST /api/register/: Register a new user.
POST /api/login/: Log in.
POST /api/logout/: Log out.

### Authentication
Token-based authentication is used to secure the API.
Include the authentication token in the Authorization header of your requests.
