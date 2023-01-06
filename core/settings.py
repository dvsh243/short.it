import mongoengine



# # # # MONGODB # # # #
async def connect_to_mongo():
    mongoengine.connect(
        db = 'EmailDashboard',
        host = "mongodb://localhost:27017",
    )
    print("[MONGO] connected to MongoDB")
# # # # MONGODB # # # #



# # # # HASHING SALT # # # #
HASHING_SALT = b'$2b$12$KsXtiOWxL/rJllAGBr3WWe'
# # # # HASHING SALT # # # #