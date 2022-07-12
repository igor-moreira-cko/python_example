# python_example
This example uses the Checkout.com SDK for making payment requests, the Frames frontend to make token requests and present the UI for card input, and FastAPI for routing requests between frontend and backend.

## Installing Fastapi
`pip install "fastapi[all]"`

## Installing Checkout.com Python SDK
`pip install checkout-sdk==3.0.0b7`

## Running the local server from main.py
`uvicorn main:app --reload`

Input your secret key in main.py, then your public key in /static/app.js
