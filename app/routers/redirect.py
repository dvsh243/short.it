from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse
from mongoengine.errors import DoesNotExist

from app.models import ShortUrlModel

router = APIRouter(
    tags = ['api'],
    prefix = ''
)


@router.get('/{shorturl}')
async def redirect(
        request: Request,
        shorturl: str
    ):
    """doesn't work on swagger"""
    print("\n\n")

    print(request.client.host)
    print(f"redirecting to --> {shorturl}")

    longurl = getLongUrl(shorturl)
    
    print("\n\n")
    if not longurl: return JSONResponse(
            content = {'res' : 'no redirection'},
            status_code = 404
        )

    return RedirectResponse(longurl)



def getLongUrl(shorturl: str):

    try:
        short_obj = ShortUrlModel.objects.get(
            shorturl = shorturl
        )
        return short_obj.longurl

    except DoesNotExist:
        return None