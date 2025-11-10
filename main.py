from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from httpx import AsyncClient, AsyncHTTPTransport

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'], allow_credentials=True)

@app.get('/api/v1/tfl/disruptions/{modes:path}')
async def get_tfl_disruptions(modes: str):
    async with AsyncClient(transport=AsyncHTTPTransport(retries=3), timeout=30) as client:
        response = await client.get(f'https://api.tfl.gov.uk/Line/Mode/{modes}/Disruption')
        response.raise_for_status()

        disruptions = []

        for disruption in response.json():
            disruptions.append({
                'category'    : disruption.get('category'),
                'type'        : disruption.get('type'),
                'description' : disruption.get('description', ''),
                'closureText' : disruption.get('closureText', ''),
            })

        return  disruptions
