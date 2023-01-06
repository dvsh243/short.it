from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse


router = APIRouter(
    tags = ['api'],
    prefix = ''
)


@router.get('/{shorturl}/analytics')
async def get_analytics(
        shorturl: str
    ):
    print("\n\n")

    print(f"getting analytics for --> {shorturl}")

    print("\n\n")
    return JSONResponse(
        content = {'res' : 'analytics'},
        status_code = 200
    )


@router.get('/{shorturl}/analytics.json')
async def get_json_analytics(
        shorturl: str
    ):
    print("\n\n")

    print(f"getting analytics for --> {shorturl}")

    print("\n\n")
    return JSONResponse(
        content = {'res' : 'analytics.json'},
        status_code = 200
    )