from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse
from mongoengine.errors import DoesNotExist
import geocoder

from app.models import ShortUrlModel, AnalyticsModel

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

    print(f"redirecting to --> {shorturl}")

    longurl = getLongUrl(shorturl)
    
    if not longurl: return JSONResponse(
            content = {'res' : 'no redirection'},
            status_code = 404
        )

    storeClickAnalytics(request, shorturl)

    print("\n\n")
    return RedirectResponse(longurl)



def getLongUrl(shorturl: str):

    try:
        short_obj = ShortUrlModel.objects.get(
            shorturl = shorturl
        )
        return short_obj.longurl

    except DoesNotExist:
        return None



def storeClickAnalytics(request, shorturl):
    print(request.client.host)

    if request.client.host.startswith('127.0.0.1'): return


    ip = geocoder.ip( request.client.host )
    print(ip.latlng)

    # ip_log = AnalyticsModel(
        # shorturl = shorturl,
        # ip_address = request.client.host,
        # city = ip.city,
        # latlng = ip.latlng
    # ).save()