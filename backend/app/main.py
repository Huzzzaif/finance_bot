#entry point for fast api
from fastapi import FastAPI, Request, HTTPException
#we need Cors as a middke ware becasue we will deploy oir front end on port 3000 and backend would be 800,
#for them to comminicate without error we need CORS - Cross-Origin-Resource_Sharing
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request,HTTPException
from backend.app.auth  import verify_firebase_token
from backend.app.retriever import get_answer_from_query
from pydantic import BaseModel
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=[],
    allow_headers=[],
)

class AskRequest(BaseModel):
    query: str

@app.get("/")
def health_check():
    return {"message" : "Finance chatbot backend running"}


#main api to ask question
@app.post("/ask")
async def ask_question(body: AskRequest):
    return get_answer_from_query(body.query)