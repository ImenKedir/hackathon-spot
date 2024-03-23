import os
from supabase import create_client 
from supabase import Client as s_client
from replicate import Client as r_client


os.environ["REPLICATE_API_TOKEN"] = "r8_PU4DJC8aqhETW1iQkBKeRXNtTsPLQ8x2FXMWZ"

url: str = 'https://tznbridngovtoxaxggxu.supabase.co'
supabase: s_client = create_client(url, supabase_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR6bmJyaWRuZ292dG94YXhnZ3h1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxMTIyNjQ4NywiZXhwIjoyMDI2ODAyNDg3fQ.3bTaC-fACKUTMG7P--TCSZUqZM3OKO_I3QBW1L0HAsw')
replicate = r_client(api_token='r8_PU4DJC8aqhETW1iQkBKeRXNtTsPLQ8x2FXMWZ')


res = supabase.storage.from_('spot').get_public_url('1.jpeg')
print(res)

# send to replicate endpoint
input = {
"image": res,
"prompt": "I'm blind. Can you describe this image for me in great detail?"
}

output = replicate.run(
    "yorickvp/llava-13b:b5f6212d032508382d61ff00469ddda3e32fd8a0e75dc39d8a4191bb742157fb",
    input=input
)

print("".join(output))