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
- [🧪 개발 환경 세팅](#-개발-환경-세팅)
- [🧱 기술 스택](#-기술-스택)
- [✨ 주요 기능](#-주요-기능)
- [📄 구성 파일](#-구성-파일)
- [🗂️ 아키텍쳐](#아키텍쳐)


---
## 🏛️ 프로젝트 소개
“법은 여전히 어렵고 멀게 느껴집니다. 

Lawmang은 사용자가 자신의 사건을 정리하고, 쟁점을 이해하며, 스스로 판단할 수 있도록 돕는 AI 기반 법률지원 서비스입니다. 

GPT, LangChain, 벡터 검색을 활용해 기술의 복잡함은 감추고, ‘이해 중심’의 경험을 제공합니다.”


---
## 🧪 개발 환경 세팅

### ① 가상환경 생성
```bash
conda create --prefix C:/conda_envs/lawmang_env python=3.11
```

### ② 가상환경 활성화
```bash
conda activate C:/conda_envs/lawmang_env
```

### ③ 패키지 설치
```bash
pip install -r requirements.txt
```

### ④ 서버 실행
```bash
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

### 1️⃣ 법률 상담 챗봇 (Legal Chatbot)
- LangGraph 기반 싱글 에이전트를 통해 문맥을 유지한 실시간 법률 상담 제공  
- 상담 흐름에 따라 관련 상담 사례 및 판례 정보 자동 연계  
- Elasticsearch, PostgreSQL, FAISS 기반 검색 엔진으로 높은 정밀도 보장


### 2️⃣ 법률 용어 검색 (Legal Terms Search)
- 사용자의 질문을 FAISS 기반 벡터 검색으로 분석해 유사 법률용어 정의 제공  
- 사전 정의 존재 시 그대로 제공, 미존재 시 GPT가 설명 생성  
- RAG(Retrieve-Augmented Generation) 방식으로 정의 + 조문 맥락까지 안내


### 3️⃣ 판례 요약 기능 (Case Summary)
- 키워드 기반 판례 검색 → API 호출로 판례 원문 확보  
- GPT가 사건개요, 판시사항, 판결요지를 요약  
- 기존 원문 중심 정보에서 벗어나, 사용자 중심 판례 이해 지원


### 4️⃣ AI 리포트 생성 (AI Report)
- 사용자 입력폼을 기반으로 GPT가 핵심 키워드 도출  
- 후속 키워드 자동 생성 → Firecrawl로 외부 자료 수집  
- 멀티 에이전트가 수집된 정보를 통합 분석하여 쟁점 및 판례가 포함된 보고서를 자동 생성


### 5️⃣ 사용자 개인화 서비스 (Personalization)
- 마이페이지 내 메모 저장 및 열람 기록 관리 기능 제공  
- 리포트 생성 및 상담 완료 시 이메일 알림 자동 발송  
- 상담·판례 열람 이력 기반 사용자 히스토리 추적 가능


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
project-root/
│
├── app/                      # 백엔드 전체 애플리케이션 루트
│   ├── __init__.py
│   ├── main.py
│
│   ├── chatbot/              # 법률상담 및 챗봇 시스템
│   │   └── agent.py
│
│   ├── chatbot_term/         # 법률 용어 검색 시스템
│   │   ├── vectorstore/
│   │   └── query_legal_terms.py
│
│   ├── core/                 # 환경설정 및 DB 관리
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── dependencies.py
│
│   ├── deepresearch/         # 웹 기반 심층 리서치 서비스
│   │   ├── core/             # API 클라이언트 및 GPT 관리
│   │   ├── prompts/          # 리포트 생성용 프롬프트 관리
│   │   ├── research/         # 키워드 생성 및 검색 처리
│   │   └── reporting/        # 리포트 빌더 및 요약 정리
│
│   ├── models/               # 데이터 모델 정의
│   │   ├── history.py
│   │   ├── memo.py
│   │   └── user.py
│
│   ├── routes/               # API 라우팅
│   │   ├── auth.py
│   │   ├── chatbot.py
│   │   ├── check.py
│   │   ├── deepresearch.py
│   │   ├── detail.py
│   │   ├── history.py
│   │   ├── legal_term.py
│   │   ├── memo.py
│   │   └── search.py
│
│   ├── schemas/              # Pydantic 기반 스키마 정의
│   │   ├── __init__.py
│   │   ├── history.py
│   │   ├── memo.py
│   │   └── user.py
│
│   └── services/             # 비즈니스 로직 처리
│       ├── __init__.py
│       ├── consultation_detail_service.py
│       ├── consultation.py
│       ├── history_service.py
│       ├── memo_service.py
│       ├── precedent_detail_service.py
│       ├── precedent_service.py
│       ├── test.py
│       └── user_service.py
│
├── .env                      # 환경변수 설정 파일
├── requirements.txt          # 의존성 목록
└── README.md
```
