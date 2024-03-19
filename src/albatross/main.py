import asyncio

from pypi_provider import PypiClient


async def main():
    async with PypiClient() as client:
        data = await client.get_json("numpy")
        print(len(data["files"]))


if __name__ == "__main__":
    asyncio.run(main())
