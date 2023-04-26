from typing import Union
import logging
from fastapi import FastAPI
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from elasticapm.handlers.logging import LoggingFilter, Formatter
import ecs_logging

app = FastAPI()


formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.addFilter(LoggingFilter())
# handler.setLevel(logging.DEBUG)
logger = logging.getLogger("elasticapm")
logger.addHandler(handler)
# logger = logging.getLogger("elasticapm")
logger.setLevel(logging.DEBUG)


apm_settings = {
    'SERVER_URL': "http://172.16.50.80:8300",
    'SERVICE_NAME': "HELPDESK",
    'SECRET_TOKEN': "",
    'CAPTURE_BODY': 'all',
    'CAPTURE_HEADERS': True,
    'COLLECT_LOCAL_VARIABLES': 'all',
    'AUTO_LOG_STACKS': True,
    'ENVIRONMENT': 'production',
    'LOG_LEVEL': 'debug'
}
apm_client = make_apm_client(apm_settings)
app.add_middleware(ElasticAPM, client=apm_client)


@app.get("/")
def read_root():
    logger.debug("Example message!")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/ping")
def pong():
    # Log a generic message with capture_message:
    # apm_client.capture_message('hello, world!')
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logger.info('Protocol problem: %s', 'SFS6ihPOBwaL6c9U0P6c', extra=d)
    for i in range(0, 10):
        logger.debug("Example message!" + str(i))
    return {"ping": "pong!"}
