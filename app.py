from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from controllers import addData, fetchData
import json
import uvicorn

app = FastAPI()

with open('./config.json') as config_file:
    config_data = json.load(config_file)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    data = fetchData.getData(config_data)
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/add_data", response_class=HTMLResponse)
async def add_data_form(request: Request):
    return templates.TemplateResponse("add_data.html", {"request": request})


@app.post("/add_data", response_class=HTMLResponse)
async def add_data(
    request: Request,
    year: int = Form(...),
    month: str = Form(...),
    category: str = Form(...),
    amount: int = Form(...),
    description: str = Form(...)
):
    addData.insertData(config_data, year+1, month, category, amount, description)
    return templates.TemplateResponse("add_data.html", {"request": request})

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
