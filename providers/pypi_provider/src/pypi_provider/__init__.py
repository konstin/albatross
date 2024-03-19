from typing import Any

from httpx import AsyncClient


class PypiClient:
    def __init__(self):
        self.client = AsyncClient()

    async def __aenter__(self):
        await self.client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.client.__aexit__(exc_type, exc, tb)

    async def get_json(self, project_name: str) -> dict[str, Any]:
        url = f"https://pypi.org/simple/{project_name}/?format=application/vnd.pypi.simple.v1+json"
        response = await self.client.get(url)
        response.raise_for_status()
        return response.json()
