from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/api/outline", response_class=PlainTextResponse)
def get_outline(country: str):
    url = f"https://en.wikipedia.org/wiki/{country}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    result = "## Contents\n\n"
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        level = int(tag.name[1])
        result += f"{'#' * level} {tag.get_text().strip()}\n\n"

    return result
