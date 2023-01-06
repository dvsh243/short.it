from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.serializers import CreateSerializer

router = APIRouter(
    tags = ['api'],
    prefix = '/api'
)


@router.post('/create')
async def create(
        request: CreateSerializer
    ):
    print("\n\n")

    print(f"creating shorturl from longurl -> {request.longurl}")

    print("\n\n")
    return JSONResponse(
        content = {'res' : 'created'},
        status_code = 200
    )