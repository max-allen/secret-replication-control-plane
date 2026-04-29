import json
import os
from contextlib import asynccontextmanager

from aiokafka import AIOKafkaProducer
from fastapi import FastAPI, Request

from .database import ping_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    ping_database()
    producer = AIOKafkaProducer(bootstrap_servers=os.environ["KAFKA_BOOTSTRAP_SERVERS"])
    await producer.start()
    app.state.kafka_producer = producer
    yield
    await producer.stop()


app = FastAPI(title="Multi-Region Secrets Control Plane", lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/secrets", status_code=202)
async def create_secret(request: Request):
    """
    NOTE: This is a mock endpoint used to confirm
    kafka has been wired properly an receives events.
    Will be replaced when CRUD API is implemented.
    """
    event = {
        "event_type": "SecretReplicationRequested",
        "path": "/foo/bar/baz",
        "target_regions": ["us-east-1", "us-east-2"],
    }
    producer: AIOKafkaProducer = request.app.state.kafka_producer
    await producer.send("secret-replication-events", json.dumps(event).encode())
    return {"status": "accepted"}
