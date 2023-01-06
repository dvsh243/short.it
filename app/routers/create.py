from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
import uuid
from mongoengine.errors import DoesNotExist

from app.serializers import CreateSerializer
from app.models import ShortUrlModel

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

    unique_id = storeShortUrl(
        request.longurl, 
        uuid.uuid4().__str__()[:7]
    )
    
    print("\n\n")
    return JSONResponse(
        content = {
            'res' : 'created',
            'shorturl' : unique_id
        },
        status_code = 200
    )



def storeShortUrl(longurl: str, unique_id: str):
    # fix hash collision (while loop until fix)

    try:
        ShortUrlModel.objects.get(
            shorturl = unique_id
        )
        raise Exception("hash collision")

    except DoesNotExist:
        ShortUrlModel(
            longurl = longurl,
            shorturl = unique_id
        ).save()
        print(f"shorturl created -> {unique_id}")
    
    return unique_id


