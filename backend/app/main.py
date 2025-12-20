from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://genai-delta.vercel.app",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    return {"reply": f"Image received: {file.filename}"}

@app.get("/")
def root():
    return {"message": "GenAI API Running"}
