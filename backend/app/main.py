# from fastapi import FastAPI, UploadFile, File, Request, Response, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from app.routers import chat
# import os

# app = FastAPI()

# # CORS — allow both local + prod
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "https://genai-delta.vercel.app",
#     ],
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Explicit OPTIONS handler (CRITICAL for Vercel)
# @app.options("/{path:path}")
# async def preflight_handler(path: str, request: Request):
#     response = Response()
#     origin = request.headers.get("origin")
#     if origin:
#         response.headers["Access-Control-Allow-Origin"] = origin
#     response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     return response

# app.include_router(chat.router)

# @app.get("/")
# def root():
#     return {"message": "GenAI API Running"}
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.routers import chat

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "https://genai-delta.vercel.app",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(chat.router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://genai-delta.vercel.app",   # frontend
        "http://localhost:3000",            # local dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(payload: dict):
    return {"message": "CORS works"}
