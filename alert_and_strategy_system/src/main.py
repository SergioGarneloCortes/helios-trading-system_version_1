from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strategy_system.strategy_manager import StrategyManager

app = FastAPI()

# CORS middleware for API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
)

@app.get("/strategy")
def run_strategy():
    strategy_manager = StrategyManager(initial_capital=10000)
    strategy_manager.run_strategy()
    return strategy_manager.evaluate()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
