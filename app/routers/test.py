from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(
    tags = ['test'],
    prefix = '/test'
)


@router.get('/')
async def test():
    print("\n\n")

    print("test")

    print("\n\n")
    return JSONResponse(
        content = {'res' : 'success'},
        status_code = 200
    )