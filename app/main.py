import logging
import sqlite3
from fastapi import FastAPI, File, UploadFile, responses
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

# Set up logging to a file
logging.basicConfig(filename='app/logs/debug.txt', level=logging.DEBUG)
logging.basicConfig(filename='app/logs/info.txt', level=logging.INFO)

# Create a connection and cursor for the SQLite database
conn = sqlite3.connect('app/database.db')
cursor = conn.cursor()

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

# Mount the 'static' folder to serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Mount the 'static' folder to serve templates
templates = Jinja2Templates(directory="app/static")

# Define a Pydantic model for the item
class Item(BaseModel):
    name: str
    description: str

@app.get("/")
async def read_root():
    # Example log message
    logging.info("Received request on the root route.")
    return {"message": "Server created!"}

@app.get("/home")
async def read_home():
    # Example log message
    logging.info("Received request on the home route.")
    return templates.TemplateResponse("home.html", {"request": "home"})

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


# Example route to retrieve all items from the database
@app.get("/items")
async def get_items():
    # Example log message
    logging.info("Received request on the items route.")

    # Retrieve all items from the database
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    return {"items": items}

# Example route to add an item to the database
@app.post("/items")
async def add_item(item: Item):
    # Example log message
    logging.info(f"Received request to add item: {item}")

    # Insert the item into the database
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (item.name, item.description))
    conn.commit()

    return {"message": "Item added successfully"}

