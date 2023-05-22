from fastapi import APIRouter
from databases.db import cursor, conn
from utils.logger import logging
from databases.models import Item

item_router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@item_router.get("/")
async def get_items():
    # Example log message
    logging.info("Received request on the items route.")

    # Retrieve all items from the database
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    return {"items": items}


@item_router.post("/")
async def add_item(item: Item):
    # Example log message
    logging.info(f"Received request to add item: {item}")

    # Insert the item into the database
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (item.name, item.description))
    conn.commit()

    return {"message": "Item added successfully"}

@item_router.delete("/{item_id}")
async def delete_item(item_id: int):
    # Example log message
    logging.info(f"Received request to delete item with id: {item_id}")

    # Delete the item from the database
    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()

    return {"message": "Item deleted successfully"}