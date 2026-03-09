from fastapi import FastAPI, HTTPException

# API created by Aisha Patel
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Aisha Patel's Calculator API!"}

# --- Part 1: Required Math Endpoints ---
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
    """Divides a by b. Handles division by zero gracefully."""
    if b == 0.0:
        raise HTTPException(status_code=400, detail="Error: Cannot divide by zero.")
    return {"operation": "divide", "a": a, "b": b, "result": a / b}

# --- Part 2: Three Additional Custom Endpoints ---
@app.get("/average/{a}/{b}/{c}")
def average(a: float, b: float, c: float):
    """Calculates the average of three numbers. Meets the >2 parameter requirement."""
    return {"operation": "average", "a": a, "b": b, "c": c, "result": (a + b + c) / 3}

@app.get("/power/{base}/{exponent}")
def power(base: float, exponent: float):
    """Calculates base raised to the power of exponent."""
    return {"operation": "power", "base": base, "exponent": exponent, "result": base ** exponent}

@app.get("/tip/{bill}/{percentage}")
def tip_calculator(bill: float, percentage: float):
    """Calculates the tip amount based on the bill and tip percentage."""
    if bill < 0 or percentage < 0:
        raise HTTPException(status_code=400, detail="Error: Bill and percentage cannot be negative.")
    
    tip_amount = bill * (percentage / 100)
    return {"operation": "tip", "bill": bill, "percentage": percentage, "result": round(tip_amount, 2)}
