from fastapi import APIRouter,Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router=APIRouter()

templates=Jinja2Templates(directory="templates/src")

@router.get("/",response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("App.js",{"request":request})