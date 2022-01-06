from fastapi import FastAPI
import utils

app = FastAPI()

@app.get("/")
def root():
    return {"element api": "hi!"}

@app.get("/symbols/")
def symbols():
    return {
        "symbols": utils.get_symbols()
    }

@app.get("/elements/")
def symbols():
    return {
        "elements": utils.get_elements()
    }

@app.get("/e/{element_symbol}")
def element(element_symbol: str):
    data = utils.get_element(element_symbol)
    return data