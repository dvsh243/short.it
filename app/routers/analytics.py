from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models import AnalyticsModel


router = APIRouter(
    tags = ['api'],
    prefix = ''
)

'''
@router.get('/{shorturl}/analytics')
async def get_analytics(
        shorturl: str
    ):
    print("\n\n")

    print(f"getting analytics for --> {shorturl}")

    print("\n\n")
    # return template response here
'''


@router.get('/{shorturl}/analytics.json')
async def get_json_analytics(
        shorturl: str
    ):
    print("\n\n")

    print(f"getting analytics for --> {shorturl}")
    analytics = getAnalytics(shorturl)

    print("\n\n")
    return JSONResponse(
        content = analytics,
        status_code = 200
    )



def getAnalytics(shorturl):
    # need to count distinct country wise click counts 

    click_count = AnalyticsModel.objects.filter(
        shorturl = shorturl
    ).count()
    

    return {
        'total_clicks' : click_count,
        'cities' : getCityMap(shorturl)
    }


def getCityMap(shorturl):

    # can store a cache of cities for fast retrieval
    cityMap = {}
    cities = AnalyticsModel.objects.distinct('city')
    # mongodb atlas free tier doesnt allow -> item_frequencies('city')

    for city in cities:
        city_clicks = AnalyticsModel.objects.filter(
            shorturl = shorturl,
            city = city
        ).count()

        cityMap[city] = city_clicks
    
    return cityMap
