"""""
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

"""
import os
import json
import asyncio
from twscrape import API, gather
from dotenv import load_dotenv

async def fetch_tweets(api, user_login, filename):
    user = await api.user_by_login(user_login)
    tweets = await gather(api.user_tweets(user.id, limit=100))  # Adjust limit as needed

    with open(filename, 'w', encoding='utf-8') as f:
        for tweet in tweets:
            f.write(f"{tweet.id}\t{tweet.rawContent}\n")

async def main():
    load_dotenv()  # load environment variables

    # Get credentials from environment variables
    username = os.getenv('TWITTER_USERNAME')
    password = os.getenv('TWITTER_PASSWORD')
    email = os.getenv('TWITTER_EMAIL')
    email_password = os.getenv('TWITTER_EMAIL_PASSWORD')

    # Delete existing database
    if os.path.exists("accounts.db"):
        os.remove("accounts.db")

    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS
    await api.pool.add_account(username, password, email, email_password)
    await api.pool.login_all()

    # Fetch tweets for JDOviedoA
    await fetch_tweets(api, "JDOviedoA", "tweets_JDOviedoA.txt")

    # Fetch tweets for GustavoBolivar
    await fetch_tweets(api, "GustavoBolivar", "tweets_GustavoBolivar.txt")
    
      # Fetch tweets for Nicolas_ramos_b
    await fetch_tweets(api, "Nicolas_ramos_b", "tweets_Nicolas_ramos_b.txt")
    
          # Fetch tweets for Rodrigo_Lara_
    await fetch_tweets(api, "Rodrigo_Lara_", "tweets_Rodrigo_Lara_.txt")   
    
      # Fetch tweets for Diego_Molano
    await fetch_tweets(api, "Diego_Molano", "tweets_Diego_Molano.txt")
    
    # Fetch tweets for JERobledo
    await fetch_tweets(api, "JERobledo", "tweets_JERobledo.txt")

    # Fetch tweets for CarlosFGalan
    await fetch_tweets(api, "CarlosFGalan", "tweets_CarlosFGalan.txt")

            # Fetch tweets for ElGeneralVargas
    await fetch_tweets(api, "ElGeneralVargas", "tweets_ElGeneralVargas.txt")

    #Fetch tweets for Alcaldia de bogota
    q = "Alcadia Bogota since:2023-01-01 until:2023-08-31"
    async for tweet in api.search(q, limit=5000):
        with open('datos.json', 'w') as json_file:
        # Write data to the file
            json.dump(tweet.json(), json_file)

if __name__ == "__main__":
    asyncio.run(main())