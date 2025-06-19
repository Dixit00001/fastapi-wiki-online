from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/outline")
async def get_outline(country: str = Query(...)):
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

    markdown = "## Contents\n\n"
    for tag in headings:
        level = int(tag.name[1])
        title = tag.get_text().strip()
        markdown += f"{'#' * level} {title}\n\n"

    return {"outline": markdown}
