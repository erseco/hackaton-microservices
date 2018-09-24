import json
import hug

router = hug.route.API(__name__)


@router.get(examples="name=world")
def hello(body, name: hug.types.text, hug_timer=3):

    return {"message": "Hello %s" % name, "took": float(hug_timer)}
