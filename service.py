import hug

from models.ExORepository import ExORepository

rep = ExORepository()


@hug.get('/status/{source_branch}')
def status_list(source_branch: str):
    rep = ExORepository()

    return rep.get_statuses(source_branch)


@hug.get('/status/{source_branch}/{repo_slug}')
def status(source_branch: str, repo_slug: str, response):
    try:
        rep = ExORepository()

        return rep.get_statuses([source_branch, repo_slug])

    except IndexError as e:
        response.status = hug.HTTP_404
        return e.__str__()
