import uvicorn
from fastapi import BackgroundTasks, FastAPI
import time


app = FastAPI()


def run():
    print("start")
    time.sleep(5)
    print("done")


@app.get("/")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(run)
    return {"success"}

uvicorn.run(app, host="127.0.0.1", port=8000)