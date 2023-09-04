import asyncio
import json
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()
    
    q = "Alcadia Bogota since:2023-01-01 until:2023-08-31"
    async for tweet in api.search(q, limit=5000):
        with open('datos.json', 'w') as json_file:
        # Write data to the file
            json.dump(tweet.json(), json_file)


if __name__ == "__main__":
    asyncio.run(main())