from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse


router = APIRouter(
    tags = ['user'],
    prefix = ''
)


@router.get('/{shorturl}')
async def redirect(
        shorturl: str
    ):
    print("\n\n")

    print(f"redirecting to --> {shorturl}")

    print("\n\n")
    return JSONResponse(
        content = {'res' : 'success'},
        status_code = 200
    )