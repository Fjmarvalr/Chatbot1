from pydantic import BaseModel

#Define a pydantic model for the schema
class ChatRequest(BaseModel):
    question: str
    user_id: str = None  # Optional user ID for tracking or personalization