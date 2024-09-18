from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

template = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/toshkent", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/toshkent")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("toshkent.html", {"request": request, "weather": f"{weather}°"})

@app.get("/andijon", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/andijon")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("andijon.html", {"request": request, "weather": f"{weather}°"})

@app.get("/samarqand", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/samarqand")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("samarqand.html", {"request": request, "weather": f"{weather}°"})

@app.get("/buxoro", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/buxoro")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("buxoro.html", {"request": request, "weather": f"{weather}°"})

@app.get("/jizzax", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/jizzax")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("jizzax.html", {"request": request, "weather": f"{weather}°"})

@app.get("/farg'ona", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/farg'ona")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("farg'ona.html", {"request": request, "weather": f"{weather}°"})

@app.get("/qashqadaryo", response_class=HTMLResponse)
async def toshkent(request: Request):
    # response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/qashqadaryo")
    # minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    # maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    # weather = (int(minimum) + int(maximum)) // 2
    weather = "ERROR"
    return template.TemplateResponse("qashqadaryo.html", {"request": request, "weather": f"{weather}°"})

@app.get("/qarshi", response_class=HTMLResponse)
async def toshkent(request: Request):
    # response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/qarshi")
    # minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    # maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    # weather = (int(minimum) + int(maximum)) // 2
    weather = "ERROR"
    return template.TemplateResponse("qarshi.html", {"request": request, "weather": f"{weather}°"})

@app.get("/surxondaryo", response_class=HTMLResponse)
async def toshkent(request: Request):
    # response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/surxondaryo")
    # minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    # maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    # weather = (int(minimum) + int(maximum)) // 2
    weather = "ERROR"
    return template.TemplateResponse("surxondaryo.html", {"request": request, "weather": f"{weather}°"})

@app.get("/navoiy", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/navoiy")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("navoiy.html", {"request": request, "weather": f"{weather}°"})

@app.get("/nukus", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/nukus")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("nukus.html", {"request": request, "weather": f"{weather}°"})

@app.get("/api", response_class=HTMLResponse)
async def api():
    html = """
Bu O'zbekiston Ob havosini topuvchi API <br>
<a href="https://ob-havo-api-y572.onrender.com" target="_blank">https://ob-havo-api-y572.onrender.com</a>
"""
    return HTMLResponse(html)