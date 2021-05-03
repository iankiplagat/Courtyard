# Courtyard Products Service

## Usage

All responses will have a jsonified form:

```json
{
  "data": "Mixed type holding the response",
  "message": "Description of what happened"
}
```

## Methods

### Fetching a product(s)

**Definition**

`GET/product`, `GET/product/<id>`

**Responses**

- `404 Not Found` if the product does not exist
- `200 OK` on success

```json
[
  {
    "id": "product id",
    "name": "product name",
    "description": "product description",
    "price": "price of the product",
    "quantity": "number of the product"
  } 
]
```

### Adding a new product

**Definition**

`POST/product`

**Arguments**

- `"id":integer` a global unique 
identifier for the specific product
- `"name":string` name of the product
- `"description":string` a short description of the product
- `"price":float` price of the product
- `"quantity":integer` number of the product items

**Response**

- `201 Created` on success

```json
[
  {
    "id": "product id",
    "name": "product name",
    "description": "product description",
    "price": "price of the product",
    "quantity": "number of the product"
  } 
]
```

## Delete a product

**Definition**

`DELETE/product/<id>`

**Response**

- `404 Not Found` if the product does not exist
- `204 No Content` on success
