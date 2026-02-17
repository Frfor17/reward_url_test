from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/reward")
async def reward_endpoint(userid: str = Query(..., description="Telegram user ID")):
    # Здесь твоя логика обработки reward для пользователя
    print(f"Получен reward для пользователя: {userid}")
    
    return {
        "status": "success",
        "message": f"Reward processed for user {userid}",
        "user_id": userid
    }
