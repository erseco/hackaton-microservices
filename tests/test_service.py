import service
import hug


class TestService:

    def test_should_return_single_status(self):
        data = hug.test.get(service, '/status/exolever-populator')
        assert data.status == '200 OK'

    def test_should_return_statuses_list(self):
        data = hug.test.get(service, '/status')
        assert data.status == '200 OK'
        assert type(data.data) == list
        assert len(data.data) == 13
