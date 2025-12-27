import httpx

async def reenviar_request(metodo, url, headers=None, json=None):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            metodo,
            url,
            headers=headers,
            json=json
        )
        return response.status_code, response.json()
