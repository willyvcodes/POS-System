import os
from dotenv import load_dotenv
import motor.motor_asyncio

load_dotenv()
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGO_URI'), tls=True, tlsAllowInvalidCertificates=True)

db = client.pos
