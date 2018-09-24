import requests
import os

BB_USER = os.environ.get('BB_USER', '')
BB_KEY = os.environ.get('BB_KEY', '')


class ExORepository:
    def load_repositories(self):
        request_url = 'https://api.bitbucket.org/2.0/repositories/exolever/'

        # Main (non exo-XXXX) repositories
        list = [
            'exolever',
            'exolever-populator',
            'end-to-end-testing',
        ]

        # BitBucket api results are paginated
        while request_url:
            r = requests.get(request_url, auth=(BB_USER, BB_KEY))

            if r.status_code != 200:
                # TODO: Raise proper exception
                # raise ApiException(r.status_code)
                pass

            result = r.json()

            for repo in result['values']:
                name = repo['full_name'].replace('exolever/', '')

                if name.startswith('exo-'):
                    list.append(name)

            request_url = result.get('next', False)

        return list

    def get_statuses(self, repos=None):
        statuses = []
        full_list = self.load_repositories()

        if repos:
            for r in repos:
                if r not in full_list:
                    raise IndexError('{} repository not found'.format(r))
        else:
            repos = full_list

        for r in repos:
            statuses.append({r: self.__get_repository_status(r)})

        return statuses

    def __get_repository_status(self, repo):
        repo_status = 'OK'
        # TODO: Fetch from BB API for the real status
        return repo_status
