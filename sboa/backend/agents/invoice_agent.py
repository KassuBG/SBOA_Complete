
def generate_invoice(order):
    return {
        "invoice_id": "INV-" + str(order["id"]),
        "amount": order["total"],
        "status": "pending"
    }
