from typing import List
import os
from html import escape
import uvicorn
from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from snek_case.core import JsonConfigurationProvider
from snek_case.sneks import CoolSnek, NormalSnek, Snek
from snek_case import _ROOT_DIRECTORY

CONFIG_FILE = os.path.join(_ROOT_DIRECTORY, "config", "config.json")

app = FastAPI(
    title="Credit Crunch",
    description="Credit Risk Analysis Web Application built on a Neural Net back-end",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="GET",
    allow_headers=["*"],
)
app.mount(
    "/config",
    StaticFiles(directory=os.path.join(_ROOT_DIRECTORY, "config")),
    name="config",
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    config = JsonConfigurationProvider(CONFIG_FILE)
    snek_type = config.get("snek_type")

    snek_types: List[Snek] = [CoolSnek(), NormalSnek()]

    snek = [s for s in snek_types if s.snek_type == snek_type][0]

    # Render in a preformatted block so ASCII art spacing and line breaks are preserved.
    html = f"""
    <html>
        <body>
            <pre>{escape(snek.snek)}</pre>
        </body>
    </html>
    """
    return HTMLResponse(content=html)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
