from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models import AnalyticsModel


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
    # return template response here



@router.get('/{shorturl}/analytics.json')
async def get_json_analytics(
        shorturl: str
    ):
    print("\n\n")

    print(f"getting analytics for --> {shorturl}")


    print("\n\n")
    return JSONResponse(
        content = showAnalytics(shorturl),
        status_code = 200
    )



def showAnalytics(shorturl):
    # need to count distinct country wise click counts 

    analytics_objs = AnalyticsModel.objects.filter(
        shorturl = shorturl
    )

    return {
        'total_clicks' : analytics_objs.count(),
    }