from fastapi import FastAPI
import os
import replicate
from supabase import create_client, Client

os.environ["REPLICATE_API_TOKEN"] = "r8_NgBhq5ope0oWJtETPlK3YKlxPFvth1u3W96ue"

url: str = 'https://tznbridngovtoxaxggxu.supabase.co'
supabase: Client = create_client(url, supabase_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR6bmJyaWRuZ292dG94YXhnZ3h1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxMTIyNjQ4NywiZXhwIjoyMDI2ODAyNDg3fQ.3bTaC-fACKUTMG7P--TCSZUqZM3OKO_I3QBW1L0HAsw')


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

@app.get("/d/{img_id}")
async def describe(img_id: str = None):
    if not img_id:
        return "INCLUDE IMG ID IN URL"


    res = supabase.storage.from_('spot').list()

    for r in res:
        print(r)

    return [res[0]]
    # send to replicate endpoint
    # input = {
    # "image": res,
    # "prompt": "I'm blind. Can you describe this image for me in great detail?"
    # }

    # output = replicate.run(
    #     "yorickvp/llava-13b:b5f6212d032508382d61ff00469ddda3e32fd8a0e75dc39d8a4191bb742157fb",
    #     input=input
    # )

    # print("".join(output))