import os
import stripe

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from typing import List

from pydantic import BaseModel
class CheckoutItem(BaseModel):
    name: str
    quantity: int
    price: int
    thumbnail: str

router = APIRouter(
    prefix = '/stripe',
    tags = ['Stripe']
)

@router.post('/create-checkout-session')
def create_checkout_session(check_items: List[CheckoutItem]):
    stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
    
    domain_url = 'https://240r2g.deta.dev/'
    # domain_url = 'https://localhost:8000/'
    new_line_items = []
    
    for product in check_items:
        new_line_items.append({
            'price_data': {
                'currency': 'usd',
                'unit_amount': product.price,
                'product_data': {
                    'name': product.name ,
                    'images': [product.thumbnail],
                },
            },
            'quantity': product.quantity,
        })

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=new_line_items,
            mode='payment',
            success_url=domain_url + 'stripe/success',
            cancel_url=domain_url + 'stripe/cancel'
        )
        return session.url
    except Exception as e:
        return {'detail': e}

@router.get("/success")
async def stripe_success():
    html_content = """
    <html>
        <head>
            <title>Payment Success</title>
            <meta http-equiv="refresh" content="3; URL=http://240r2g.deta.dev" />
        </head>
        <body>
            <h1>Thank You! Payment Success</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@router.get("/cancel", response_class=HTMLResponse)
async def stripe_cancel():
    html_content = """
    <html>
        <head>
            <title>Payment Canceled</title>
        </head>
        <body>
            <h1>Payment Was Canceled!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
