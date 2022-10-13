import os
import stripe

from fastapi import APIRouter
from typing import List

from pydantic import BaseModel
class CheckoutItem(BaseModel):
    name: str
    quantity: int
    price: int
    thumbnail: str

router = APIRouter(
    prefix = '/api/stripe',
    tags = ['Stripe']
)

@router.post('/create-checkout-session')
def create_checkout_session(check_items: List[CheckoutItem]):
    stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
    
    domain_url = 'https://240r2g.deta.dev'
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
            success_url=domain_url,
            cancel_url=domain_url
        )
        return session.url
    except Exception as e:
        return {'detail': e}
