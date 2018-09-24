import hug

from models.ExORepository import ExORepository

rep = ExORepository()


@hug.get('/status')
def status_list():
    rep = ExORepository()

    return rep.get_statuses()


@hug.get('/status/{repo}')
def status(repo: str, response):
    try:
        rep = ExORepository()

        return rep.get_statuses([repo])
    except IndexError as e:
        response.status = hug.HTTP_404
        return e.__str__()
