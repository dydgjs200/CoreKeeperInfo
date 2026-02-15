# CoreKeeperInfo

Claude로 개발하는 코어키퍼 정보 웹 페이지

## Tech Stack

| 구분 | 기술 |
|------|------|
| Frontend | React + Vite + TypeScript |
| Backend | FastAPI (Python) |
| Database | PostgreSQL |
| ORM | SQLAlchemy |

## Project Structure

```
CoreKeeperInfo/
├── frontend/               # React + Vite + TypeScript
│   ├── src/
│   │   ├── components/     # 재사용 UI 컴포넌트
│   │   ├── pages/          # 페이지 컴포넌트
│   │   ├── hooks/          # 커스텀 훅
│   │   ├── services/       # API 호출
│   │   ├── types/          # TypeScript 타입 정의
│   │   └── assets/         # 이미지, 아이콘
│   └── package.json
├── backend/                # FastAPI
│   ├── app/
│   │   ├── api/            # 라우터/엔드포인트
│   │   ├── models/         # SQLAlchemy 모델
│   │   ├── schemas/        # Pydantic 스키마
│   │   ├── services/       # 비즈니스 로직
│   │   └── core/           # 설정, DB 연결
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## Getting Started

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
