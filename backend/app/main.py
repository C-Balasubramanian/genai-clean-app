from fastapi import FastAPI, UploadFile, File, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # IMPORTANT for Vercel
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handle preflight explicitly (Vercel fix)
@app.options("/{path:path}")
async def preflight_handler(request: Request, path: str):
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

app.include_router(chat.router)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    return {"reply": f"Image received: {file.filename}"}

@app.get("/")
def root():
    return {"message": "GenAI API Running"}
