from flask import Flask, jsonify, request
from service.models import Product

app = Flask(__name__)


@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.get_json() or {}
    product = Product(
        name=data.get("name"),
        description=data.get("description"),
        price=data.get("price", 0.0),
        category=data.get("category"),
        available=data.get("available", True),
    )
    product.create()
    return jsonify(product_to_dict(product)), 201


@app.route("/api/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product_to_dict(product)), 200


@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json() or {}
    for field in ("name", "description", "price", "category", "available"):
        if field in data:
            setattr(product, field, data[field])

    product.update()
    return jsonify(product_to_dict(product)), 200


@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    product.delete()
    return jsonify({"message": "Product has been Deleted!"}), 200


@app.route("/api/products", methods=["GET"])
def list_products():
    products = Product.all()
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = [p for p in products if p.name == name]
    if category:
        products = [p for p in products if p.category == category]
    if available is not None:
        products = [
            p for p in products
            if p.available == (available.lower() == "true")
        ]

    return jsonify([product_to_dict(p) for p in products]), 200


def product_to_dict(product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "category": product.category,
        "available": product.available,
    }


if __name__ == "__main__":
    app.run(debug=True)