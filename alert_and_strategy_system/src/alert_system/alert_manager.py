from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from alert_system.telegram_alert import TelegramAlert
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Alert(BaseModel):
    symbol: str
    signal: str

app = FastAPI()

class AlertManager:
    def __init__(self):
        self.telegram_alert = TelegramAlert()

    def send_alert(self, chat_id: int, message: str):
        self.telegram_alert.send_message(chat_id, message)

@app.post("/alert")
def create_alert(data: Alert):
    chat_id = int(os.getenv('YOUR_CHAT_ID'))  # Replace with your chat ID
    alert_manager = AlertManager()
    alert_manager.send_alert(chat_id, message=data.signal)
    return {"message": "Alert sent"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
