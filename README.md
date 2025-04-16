# 💼 Lawmang Backend API v1.0

> **코드랩 아카데미 AICC 4기 2팀**  
> **개발기간: 2025. 01. 21 ~ 2025. 04. 15**


## 👩‍👩‍👧‍👦 웹개발팀 소개
> **이영선**, **황현지**, **천서영**, **박준호**, **김용주**


## 배포 주소
> **프론트 서버** : https://lawmang-front.vercel.app<br>
> **프론트 깃허브 주소** : https://github.com/ChloeLee01/lawmang_front
> **API 문서 URL** : https://lawmangback.aicc4hyeonji.site/docs


## 📚 목차

- [🏛️ 프로젝트 소개](#-프로젝트-소개)
- [🚀 시작 가이드](#-시작-가이드)
- [🧱 기술 스택](#-기술-스택)
- [✨ 주요 기능](#-주요-기능)
- [📄 구성 파일](#-구성-파일)
- [🗂️ 아키텍쳐](#-아키텍쳐)


---
## 🏛️ 프로젝트 소개
“법은 여전히 어렵고 멀게 느껴집니다. 

Lawmang은 사용자가 자신의 사건을 정리하고, 쟁점을 이해하며, 스스로 판단할 수 있도록 돕는 AI 기반 법률지원 서비스입니다. 

GPT, LangChain, 벡터 검색을 활용해 기술의 복잡함은 감추고, ‘이해 중심’의 경험을 제공합니다.”


---
## 🧪 개발 환경 세팅

1. 가상환경 생성  
```bash
conda create --prefix C:/conda_envs/lawmang_env python=3.11

- 가상환경 활성화
conda activate C:/conda_envs/lawmang_env

- 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload

```

---
## 🧱 기술 스택

### Backend
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CA5047?style=for-the-badge)
![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?style=for-the-badge&logo=uvicorn&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-0099cc?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-000000?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-003366?style=for-the-badge)
![Firecrawl](https://img.shields.io/badge/Firecrawl-FF6F00?style=for-the-badge)


---
## ✨ 주요 기능

### 1️ 법률 상담 챗봇 (Legal Chatbot)
- 사용자의 질문을 분석하여 즉각적이고 정확한 법률 상담 제공  
- 상담 사례 및 판례 검색을 통한 상세한 법률 정보 제공  
- Elasticsearch, PostgreSQL, FAISS 기반 검색 엔진 활용으로 높은 정확도 보장

### 2️⃣ 법률 용어 검색 서비스 (Legal Terms Search)
- 사용자가 궁금한 법률 전문 용어에 대해 정의와 설명을 빠르게 제공
- 벡터 기반의 고속 검색을 통해 관련된 법률 용어를 쉽고 정확하게 검색 가능
- RAG(Retrieve-Augmented Generation) 방식을 활용하여, 외부 지식(DB, 문서 등)을 검색(Retrieve)한 뒤, LLM이 그 내용을 바탕으로 응답을 생성(Generate)함으로써
보다 정확하고 맥락 있는 정보를 제공

### 3️⃣ 딥 리서치 서비스 (Deep Research)
- 특정 법률 이슈에 대해 웹 기반의 심층 리서치 수행
- Firecrawl, GPT 를 활용한 최신 법률 정보 및 자료 수집
- 수집된 자료를 바탕으로 요약 보고서 및 세부 리포트 생성

### 4️⃣ 사용자 개인화 서비스 (Personalization)
- 상담 기록 및 법률 상담 이력 관리
- 메모 작성 및 개인 기록 관리 기능 제공
- 사용자 맞춤형 콘텐츠 제공 (최근 조회한 상담, 개인 히스토리 등)

---
## 📄 구성 파일

| 기능                 | 설명                                       | 주요 파일 및 폴더                       |
|----------------------|--------------------------------------------|------------------------------------------|
| API 라우팅            | HTTP 요청 경로 정의 및 엔드포인트 연결       | `routes/*.py`                            |
| 데이터 모델           | ORM 기반 DB 모델 정의                       | `models/*.py`                            |
| 데이터 스키마         | 요청/응답 데이터 유효성 검증 (Pydantic)      | `schemas/*.py`                           |
| 비즈니스 로직         | 각 기능별 서비스 로직 처리                   | `services/*.py`                          |
| 환경설정 및 DB 관리    | DB 연결, 환경 변수, 종속성 관리              | `core/*.py`                              |
| 법률 상담 챗봇        | LLM 기반 상담 기능 구현                     | `chatbot/*.py`, `chatbot/tool_agents/*`  |
| 법률 용어 검색        | 벡터 검색 기반 법률 용어 검색 기능           | `chatbot_term/*.py`                      |
| 심층 웹 리서치        | GPT 기반 외부 자료 수집 및 요약 보고서 생성  | `deepresearch/*.py`                      |

---
## 🗂️ 아키텍쳐 
### 시스템 구조

```
app/                    # 백엔드 전체 애플리케이션 루트
│
├── chatbot/              # 법률상담 및 챗봇 시스템
│   └── agent.py
│
├── chatbot_term/         # 법률 용어 검색 시스템
│   ├── vectorstore
│   └── query_legal_terms.py
│
├── core/                 # 핵심 시스템 환경설정 및 DB 관리
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   └── dependencies.py
│
├── deepresearch/         # 웹 기반 심층 리서치 서비스
│   ├── core/             # API 클라이언트 및 GPT 관리
│   ├── prompts/          # 리포트 생성 및 시스템 프롬프트 관리
│   ├── research/         # 키워드 생성 및 검색 처리 관리
│   └── reporting/        # 리포트 빌더 및 결과 보고서 생성
│
├── models/               # 데이터 모델 정의 (사용자, 히스토리 등)
│   ├── history.py
│   ├── memo.py
│   └── user.py
│
├── routes/               # API 라우팅 관리
│   ├── auth.py
│   ├── chatbot.py
│   ├── check.py
│   ├── deepresearch.py
│   ├── detail.py
│   ├── history.py
│   ├── legal_term.py
│   ├── memo.py
│   └── search.py
│
├── schemas/              # 데이터 스키마 관리 (Pydantic 모델)
│   ├── __init__.py
│   ├── history.py
│   ├── memo.py
│   └── user.py
│
├── services/             # 비즈니스 로직 및 서비스 로직 관리
│   ├── __init__.py
│   ├── consultation_detail_service.py
│   ├── consultation.py
│   ├── history_service.py
│   ├── memo_service.py
│   ├── precedent_detail_service.py
│   ├── precedent_service.py
│   ├── test.py
│   └── user_service.py
│
├── __init__.py
└── main.py
```

