from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def handle_command():
    cmd = input()
    if cmd == "0":
        return {cmd}
    elif cmd == "1":
        return {cmd}
    else:
        return {"Invalid input. Please enter a valid cmd."}