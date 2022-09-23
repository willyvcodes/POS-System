import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.5i8llmr.mongodb.net/test"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, tls=True, tlsAllowInvalidCertificates=True)

db = client.pos
