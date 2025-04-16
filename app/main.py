import bcrypt
from types import SimpleNamespace

if not hasattr(bcrypt, "__about__"):
    bcrypt.__about__ = SimpleNamespace(__version__=bcrypt.__version__)

from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from app.core.config import settings
from app.routes import auth, check, detail, search, memo, history, legal_term, deepresearch, chatbot
from app.core.database import init_db
import os
import signal
import sys
import asyncio
from dotenv import load_dotenv

load_dotenv()
# test

# ✅ FastAPI 애플리케이션 생성 (기본 응답을 ORJSONResponse로 설정)
app = FastAPI(default_response_class=ORJSONResponse)

# ✅ CORS 설정 (React와 연결할 경우 필수)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lawmang-front.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 라우터 등록
app.include_router(check.router, prefix="/api/check", tags=["check"])    
app.include_router(search.router, prefix="/api/search", tags=["search"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(detail.router, prefix="/api/detail", tags=["detail"])
app.include_router(memo.router, prefix="/api/mylog/memo", tags=["memo"])
app.include_router(history.router, prefix="/api/mylog/history", tags=["history"])
app.include_router(chatbot.router, prefix="/api/chatbot", tags=["chatbot"])
app.include_router(legal_term.router, prefix="/api/chatbot_term", tags=["legal-term"])
app.include_router(deepresearch.router, prefix="/api/deepresearch", tags=["deepresearch"])

# ✅ 기본 엔드포인트 (테스트용)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# ✅ 서버 시작 시 데이터베이스 초기화
@app.on_event("startup")
def on_startup():
    init_db()  # ✅ `Base.metadata.create_all(bind=engine)` 제거

# ✅ 공통 예외 처리 (404 & 500 에러 핸들러)
@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    return {"error": "해당 경로를 찾을 수 없습니다."}  # ✅ CORSMiddleware가 헤더 붙여줌

@app.exception_handler(500)
async def internal_server_error_handler(request: Request, exc: HTTPException):
    return {
        "error": "서버 내부 오류가 발생했습니다.",
        "detail": str(exc.detail) if hasattr(exc, "detail") else "알 수 없는 오류"
    }


# ✅ 종료 시그널 핸들러 (FastAPI 종료 시 오류 방지)
def signal_handler(sig, frame):
    print("서버를 정상적으로 종료합니다...")
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.call_soon_threadsafe(loop.stop)  # ✅ 안전한 이벤트 루프 종료
    except RuntimeError:
        pass
    sys.exit(0)

# ✅ 서버 시작 시 라우터 경로 로깅
@app.on_event("startup")
def log_routes_on_startup():
    print("\n📌 [FastAPI 등록된 라우터 경로]")
    print("=" * 50)
    for route in app.routes:
        if route.path.startswith("/api/auth/auth"):
            print(f"❌ 중복된 경로: {route.path}")
        else:
            print(f"✅ 정상 경로: {route.path}")
    print("=" * 50)