import mongoengine



# # # # MONGODB # # # #
async def connect_to_mongo():
    mongoengine.connect(
        db = 'ShortURL',
        host = "mongodb+srv://devesh243:Qwerty12341234@testcluster.lnfr7wa.mongodb.net/?retryWrites=true&w=majority",
        # host = "mongodb://localhost:27017",
    )
    print("[MONGO] connected to MongoDB")
# # # # MONGODB # # # #