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
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/qashqadaryo")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("qashqadaryo.html", {"request": request, "weather": f"{weather}°"})

@app.get("/qarshi", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/qarshi")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("qarshi.html", {"request": request, "weather": f"{weather}°"})

@app.get("/surxondaryo", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/surxondaryo")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
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

@app.get("/xiva", response_class=HTMLResponse)
async def toshkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/xiva")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("xiva.html", {"request": request, "weather": f"{weather}°"})

@app.get("/baliqchi", response_class=HTMLResponse)
async def baliqchi(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/baliqchi")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("baliqchi.html", {"request": request, "weather": f"{weather}°"})

@app.get("/sirdaryo", response_class=HTMLResponse)
async def sirdaryo(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/sirdaryo")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("sirdaryo.html", {"request": request, "weather": f"{weather}°"})

@app.get("/bekobod", response_class=HTMLResponse)
async def bekobod(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/bekobod")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("bekobod.html", {"request": request, "weather": f"{weather}°"})

@app.get("/olmaliq", response_class=HTMLResponse)
async def olmaliq(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/olmaliq")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("olmaliq.html", {"request": request, "weather": f"{weather}°"})

@app.get("/oltiariq", response_class=HTMLResponse)
async def oltiariq(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/oltiariq")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("oltiariq.html", {"request": request, "weather": f"{weather}°"})

@app.get("/oltinsoy", response_class=HTMLResponse)
async def oltinsoy(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/oltinsoy")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("oltiariq.html", {"request": request, "weather": f"{weather}°"})

@app.get("/oqtosh", response_class=HTMLResponse)
async def oqtosh(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/oqtosh")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("oqtosh.html", {"request": request, "weather": f"{weather}°"})

@app.get("/parkent", response_class=HTMLResponse)
async def parkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/parkent")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("parkent.html", {"request": request, "weather": f"{weather}°"})

@app.get("/parkent", response_class=HTMLResponse)
async def parkent(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/parkent")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("parkent.html", {"request": request, "weather": f"{weather}°"})

@app.get("/sherobod", response_class=HTMLResponse)
async def sherobod(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/sherobod")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("sherobod.html", {"request": request, "weather": f"{weather}°"})

@app.get("/shofirkon", response_class=HTMLResponse)
async def shofirkon(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/shofirkon")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("shofirkon.html", {"request": request, "weather": f"{weather}°"})

@app.get("/termiz", response_class=HTMLResponse)
async def termiz(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/termiz")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("termiz.html", {"request": request, "weather": f"{weather}°"})

@app.get("/zarafshon", response_class=HTMLResponse)
async def zarafshon(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/zarafshon")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("zarafshon.html", {"request": request, "weather": f"{weather}°"})

@app.get("/buxoro", response_class=HTMLResponse)
async def buxoro(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/buxoro")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("buxoro.html", {"request": request, "weather": f"{weather}°"})

@app.get("/guliston", response_class=HTMLResponse)
async def guliston(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/guliston")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("guliston.html", {"request": request, "weather": f"{weather}°"})

@app.get("/bog'ot", response_class=HTMLResponse)
async def bogot(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/bog'ot")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("bog'ot.html", {"request": request, "weather": f"{weather}°"})

@app.get("/bulung'ur", response_class=HTMLResponse)
async def bulungur(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/bulung'ur")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("bulung'ur.html", {"request": request, "weather": f"{weather}°"})

@app.get("/denov", response_class=HTMLResponse)
async def denov(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/denov")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("denov.html", {"request": request, "weather": f"{weather}°"})

@app.get("/chiroqchi", response_class=HTMLResponse)
async def chiroqchi(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/chiroqchi")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("chiroqchi.html", {"request": request, "weather": f"{weather}°"})

@app.get("/dehqonobod", response_class=HTMLResponse)
async def dehqonobod(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/dehqonobod")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("dehqonobod.html", {"request": request, "weather": f"{weather}°"})

@app.get("/ishtixon", response_class=HTMLResponse)
async def ishtixon(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/ishtixon")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("ishtixon.html", {"request": request, "weather": f"{weather}°"})

@app.get("/payariq", response_class=HTMLResponse)
async def payariq(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/payariq")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("payariq.html", {"request": request, "weather": f"{weather}°"})

@app.get("/qamashi", response_class=HTMLResponse)
async def dehqonobod(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/qamashi")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("qamashi.html", {"request": request, "weather": f"{weather}°"})

@app.get("/qumqo'rg'on", response_class=HTMLResponse)
async def qumqorgon(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/qumqo'rg'on")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("qumqo'rg'on.html", {"request": request, "weather": f"{weather}°"})

@app.get("/qo'qon", response_class=HTMLResponse)
async def qoqon(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/qo'qon")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("qo'qon.html", {"request": request, "weather": f"{weather}°"})

@app.get("/kitob", response_class=HTMLResponse)
async def kitob(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/kitob")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("kitob.html", {"request": request, "weather": f"{weather}°"})

@app.get("/jondor", response_class=HTMLResponse)
async def jondor(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/jondor")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("jordon.html", {"request": request, "weather": f"{weather}°"})

@app.get("/kokand", response_class=HTMLResponse)
async def kokand(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/kokand")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("kokand.html", {"request": request, "weather": f"{weather}°"})

@app.get("/koson", response_class=HTMLResponse)
async def koson(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/koson")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("koson.html", {"request": request, "weather": f"{weather}°"})

@app.get("/marg'ilon", response_class=HTMLResponse)
async def margilon(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/marg'ilon")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("marg'ilon.html", {"request": request, "weather": f"{weather}°"})

@app.get("/nurobod", response_class=HTMLResponse)
async def nurobod(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/nurobod")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("nurobod.html", {"request": request, "weather": f"{weather}°"})

@app.get("/quva", response_class=HTMLResponse)
async def quva(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/quva")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("quva.html", {"request": request, "weather": f"{weather}°"})

@app.get("/rishton", response_class=HTMLResponse)
async def rishton(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/rishton")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("rishton.html", {"request": request, "weather": f"{weather}°"})

@app.get("/romitan", response_class=HTMLResponse)
async def romitan(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/romitan")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("romitan.html", {"request": request, "weather": f"{weather}°"})

@app.get("/shahrisabz", response_class=HTMLResponse)
async def shahrisabz(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/shahrisabz")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("shahrisabz.html", {"request": request, "weather": f"{weather}°"})

@app.get("/urgut", response_class=HTMLResponse)
async def urgut(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/urgut")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("urgut.html", {"request": request, "weather": f"{weather}°"})

@app.get("/urganch", response_class=HTMLResponse)
async def urganch(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/urganch")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("urganch.html", {"request": request, "weather": f"{weather}°"})

@app.get("/uchquduq", response_class=HTMLResponse)
async def uchquduq(request: Request):
    response = requests.get("https://ob-havo-api-y572.onrender.com/api/v1/obhavo/uchquduq")
    minimum = str(response.json()[0]['bugun'][0]['harorat'][0]['min']).replace('°', '')
    maximum = str(response.json()[0]['bugun'][0]['harorat'][1]['max']).replace('°', '')
    weather = (int(minimum) + int(maximum)) // 2
    return template.TemplateResponse("uchquduq.html", {"request": request, "weather": f"{weather}°"})

@app.get("/api", response_class=HTMLResponse)
async def api():
    html = """
Bu O'zbekiston Ob havosini topuvchi API <br>
<a href="https://ob-havo-api-y572.onrender.com" target="_blank">https://ob-havo-api-y572.onrender.com</a>
"""
    return HTMLResponse(html)