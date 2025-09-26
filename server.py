# calculator_server.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ast
import operator

app = FastAPI()

# Define allowed operators
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

# Request schema
class ExpressionRequest(BaseModel):
    expr: str

# Safe expression evaluator
def safe_eval(expr: str):
    try:
        tree = ast.parse(expr, mode='eval')

        def _eval(node):
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                else:
                    raise ValueError("Only numeric constants are allowed")
            elif isinstance(node, ast.BinOp):
                left = _eval(node.left)
                right = _eval(node.right)
                op_type = type(node.op)
                if op_type in operators:
                    return operators[op_type](left, right)
                else:
                    raise ValueError("Unsupported binary operator")
            elif isinstance(node, ast.UnaryOp):
                operand = _eval(node.operand)
                op_type = type(node.op)
                if op_type in operators:
                    return operators[op_type](operand)
                else:
                    raise ValueError("Unsupported unary operator")
            else:
                raise ValueError("Invalid expression")

        return _eval(tree)

    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {e}")

# Route for calculation
@app.post("/calculate")
def calculate(req: ExpressionRequest):
    result = safe_eval(req.expr)
    return {"result": result}
