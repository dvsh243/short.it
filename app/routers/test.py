from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    tags = ['test'],
    prefix = ''
)


@router.get('/')
async def welcome(
        request: Request
    ):
    return JSONResponse(
        content = {
            'server' : 'nginx',
            'port' : 8000,
            'headers' : jsonable_encoder(request.headers),
            'client' : request.client
        },
        status_code = 200
    )


@router.get('/test')
async def test():
    print("\n\n")

    print("test")

    print("\n\n")
    return JSONResponse(
        content = {'res' : 'success'},
        status_code = 200
    )

