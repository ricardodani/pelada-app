from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Root of the app, will serve the frontend that consumes the API"""
    context = {
        "title": "Pelada App!",
        "heading": "Welcome!",
        "content": "This is my first FastAPI app!"
    }
    return templates.TemplateResponse(
        "index.html", {"request": request, "context": context}
    )


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Example endpoint"""
    return {"item_id": item_id, "q": q}
