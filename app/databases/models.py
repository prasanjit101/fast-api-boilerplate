from pydantic import BaseModel

# Define a Pydantic model for the item
class Item(BaseModel):
    name: str
    description: str