import mongoengine



# # # # MONGODB # # # #
async def connect_to_mongo():
    mongoengine.connect(
        db = 'ShortURL',
        host = "mongodb://localhost:27017",
    )
    print("[MONGO] connected to MongoDB")
# # # # MONGODB # # # #