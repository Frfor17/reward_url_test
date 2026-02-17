from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/reward")
async def reward_endpoint(userid: str = Query(..., description="Telegram user ID")):
    # Adsgram шлёт буквально "[userId]" - убираем скобки если есть
    clean_userid = userid.replace("[userId]", "").strip()
    
    print(f"Получен reward для пользователя: {clean_userid} (исходный: {userid})")
    
    return {
        "status": "success",
        "message": f"Reward processed for user {clean_userid}",
        "user_id": clean_userid
    }
