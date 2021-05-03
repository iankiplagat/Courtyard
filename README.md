# Courtyard Products Service

## Usage

All responses will have a jsonified form:

```json
{
  "data": "Mixed type holding the response",
  "message": "Description of what happened"
}
```

### Methods

**Definition**

`POST/product`

**Responses**

- `200 OK` on success

```json
[
  {
    "name": "product name",
    "description": "product description",
    "price": "price of the product",
    "quantity": "number of the product"
  } 
]
```