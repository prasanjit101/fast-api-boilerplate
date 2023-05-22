from datetime import datetime
import logging
from fastapi import FastAPI, File, UploadFile, responses, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# imports
from app.databases.db import conn, cursor
from app.api.routes import item_router
from app.utils.logger import logging
from app.utils.middleware import LoggingMiddleware

# Add middleware

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
''')
conn.commit()

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # log time
    logging.info(f"Server started: {datetime.now()}")

# Add middleware
app.add_middleware(LoggingMiddleware)

# Add routes
app.include_router(item_router)

# Mount the 'static' folder to serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Mount the 'static' folder to serve templates
templates = Jinja2Templates(directory="app/static")

@app.get("/")
async def read_root():
    # Example log message
    logging.info("Received request on the root route.")
    return {"message": "Server running!"}

@app.get("/home")
async def read_home(request: Request):
    # Example log message
    logging.info("Received request on the home route.")
    return templates.TemplateResponse("index.html", {"request": request, "title": "home"})

# file upload route
@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
    # Example log message
    logging.info(f"Received request to upload file: {file.filename}")
    # save file
    with open(f"app/static/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    return {"message": "File uploaded successfully"}

# file download route
@app.get("/download/{file_name}")
async def download_file(file_name: str):
    # Example log message
    logging.info(f"Received request to download file: {file_name}")
    return responses.FileResponse(f"app/static/{file_name}", media_type="application/octet-stream", filename=file_name)


@app.on_event("shutdown")
async def shutdown_event():
    logging.info(f"Server stopped: {datetime.now()}")