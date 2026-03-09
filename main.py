---

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
return JSONResponse(
status_code=422,
content={"detail": "Error: All arguments must be valid numbers."}
)

@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
if exc.status_code == 404:
return JSONResponse(
status_code=422,
content={"detail": "Error: Missing parameter or invalid route."}
)
return JSONResponse(
status_code=exc.status_code,
content={"detail": exc.detail}
)

@app.get("/")
def read_root():
return {"message": "Welcome to Aisha Patel's Calculator API!"}

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
"""Adds two numbers."""
return {"operation": "add", "a": a, "b": b, "result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
"""Subtracts b from a."""
return {"operation": "subtract", "a": a, "b": b, "result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
"""Multiplies two numbers."""
return {"operation": "multiply", "a": a, "b": b, "result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
"""Divides a by b. Handles division by zero with a 422 error."""
if b == 0.0:
raise HTTPException(status_code=422, detail="Error: Cannot divide by zero.")
return {"operation": "divide", "a": a, "b": b, "result": a / b}

@app.get("/average/{a}/{b}/{c}")
def average(a: float, b: float, c: float):
"""Calculates the average of three numbers."""
return {"operation": "average", "a": a, "b": b, "c": c, "result": (a + b + c) / 3}

@app.get("/power/{base}/{exponent}")
def power(base: float, exponent: float):
"""Calculates base raised to the power of exponent."""
return {"operation": "power", "base": base, "exponent": exponent, "result": base ** exponent}

@app.get("/tip/{bill}/{percentage}")
def tip_calculator(bill: float, percentage: float):
"""Calculates tip. Returns 422 if inputs are negative."""
if bill < 0 or percentage < 0:
raise HTTPException(status_code=422, detail="Error: Bill and percentage cannot be negative.")

```
tip_amount = bill * (percentage / 100)
return {"operation": "tip", "bill": bill, "percentage": percentage, "result": round(tip_amount, 2)}

```

---
