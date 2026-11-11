# RAG Lab

Dự án học cách xây dựng trợ lý hỏi đáp tài liệu bằng Python và FastAPI.

## Trạng thái hiện tại

- Có API kiểm tra liveness.
- Có cấu hình ứng dụng bằng biến môi trường.
- Có kiểm thử tự động.
- Đang xây dựng dữ liệu mẫu và bộ câu hỏi đánh giá RAG.

## Yêu cầu

- Python 3.12
- uv

## Cài đặt

```powershell
uv sync --locked
Copy-Item .env.example .env
```

Chỉ sao chép `.env.example` khi chưa có file `.env`.

## Chạy API

```powershell
uv run uvicorn app.main:create_app --factory --reload --host 127.0.0.1 --port 8000
```

Tài liệu API: http://127.0.0.1:8000/docs

## Kiểm tra

```powershell
uv run python -m pytest -q
uv run ruff check .
uv run ruff format --check .
```

## Dữ liệu

- `data/sample/`: tài liệu minh họa được lưu trong Git.
- `data/private/`: tài liệu riêng, không lưu trong Git.
- `data/generated/`: dữ liệu sinh ra, không lưu trong Git.
- `evals/`: câu hỏi và đáp án tham chiếu phục vụ đánh giá.