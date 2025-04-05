#entry point for fast api
from fastapi import FastAPI
#we need Cors as a middke ware becasue we will deploy oir front end on port 3000 and backend would be 800,
#for them to comminicate without error we need CORS - Cross-Origin-Resource_Sharing
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request,HTTPException
from app.auth  import verify_firebase_token
from app.retriever import retrieve_context

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=[],
    allow_headers=[],
)

@app.get("/")
def read_root():
    return {"message" : "Finance chatbot backend running"}

#main api to ask question
@app.post("/ask")
async def ask_question(request: Request):
    try:
        context = retrieve_context(Request)
        mock_answer = "This is the mock answer"
        return {"answer": mock_answer}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))