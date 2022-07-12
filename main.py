import checkout_sdk
from checkout_sdk.environment import Environment
from checkout_sdk.common.enums import Currency
from checkout_sdk.payments.payments import PaymentRequest

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


class Token(BaseModel):
    token: str


app = FastAPI()
''
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.post("/pay")
async def payment(token: Token):
    sk = ""

    checkout_api = checkout_sdk.DefaultSdk() \
        .secret_key(sk) \
        .environment(Environment.sandbox()) \
        .build()

    payment_request = PaymentRequest()
    card_token = token.token
    source = {"type": "token", "token": card_token}
    payment_request.source = source
    payment_request.reference = "Python token test"
    payment_request.amount = 2500
    payment_request.currency = Currency.GBP
    payment_request.capture = True

    checkout_api.payments.request_payment(payment_request)
