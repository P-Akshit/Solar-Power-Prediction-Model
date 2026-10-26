from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import joblib as jb

app = FastAPI()

solar_model = jb.load("solar_model.plk")
a_model = jb.load("a_model.plk")


class get_solar_data:
    pass

class get_a_data:
    pass

@app.post('/solar')
def solar():
    pass


@app.post('/a')
def a():
    pass