import motor.motor_asyncio
from config import DB_URL, DB_NAME

class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.user_col = self.db.user
        self.movie_col = self.db.movies  # New collection for movies

    def new_movie(self, title, link):
        return {
            "title": title,
            "link": link
        }

    async def add_movie(self, title, link):
        movie = self.new_movie(title, link)
        await self.movie_col.insert_one(movie)

    async def search_movies(self, query, offset=0, limit=10):
        results = self.movie_col.find(
            {"title": {"$regex": query, "$options": "i"}}
        ).skip(offset).limit(limit)
        return await results.to_list(length=limit)

    async def total_movies_count(self):
        return await self.movie_col.count_documents({})

db = Database(DB_URL, DB_NAME)
