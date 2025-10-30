from fastapi import FastAPI
from fastapi.responses import HTMLResponse # <-- BƯỚC 1: IMPORT CÔNG CỤ MỚI

app = FastAPI(
    title="API Chào Mừng Đỉnh Cao",
    description="Một API đơn giản để triển khai lên AWS.",
    version="1.0.0",
)

@app.get("/")
def read_root():
    """
    Endpoint gốc trả về một thông điệp chào mừng JSON.
    """
    return {"message": "Chào mừng đến với hành trình DevOps cùng FastAPI và AWS!"}

# --- BẮT ĐẦU PHẦN NÂNG CẤP ---

@app.get("/api/v1/greeting", response_class=HTMLResponse) # <-- BƯỚC 3 (Cách khác): Khai báo kiểu phản hồi
async def get_greeting() -> HTMLResponse: # <-- BƯỚC 3: CẬP NHẬT KIỂU TRẢ VỀ
    """
    Endpoint trả về một trang HTML chào mừng lộng lẫy từ đám mây AWS.
    """
    # BƯỚC 2: ĐỌC NỘI DUNG TỪ FILE HTML
    with open("templates/greeting.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # TRẢ VỀ MỘT PHẢN HỒI HTML
    return HTMLResponse(content=html_content, status_code=200)

# --- KẾT THÚC PHẦN NÂNG CẤP ---
