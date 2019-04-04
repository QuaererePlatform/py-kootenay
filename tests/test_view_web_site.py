import json
from unittest import mock

from willamette.models import WebSiteModel
# from willamette.schemas.web_sites import WebSiteSchema


class TestWebSiteView:
    @mock.patch('willamette.views.api_v1.web_sites.get_db')
    def test_index(self, mock_get_db, client):
        web_site_data = [
            {"_key": "36733",
             "inLanguage": "en_us",
             "url": "https://www.vice.com/en_us", },
            {"_key": "47050",
             "inLanguage": "en_us",
             "url": "https://news.vice.com/en_us", },
            {"_key": "47885",
             "inLanguage": "en_us",
             "url": "https://broadly.vice.com/en_us", }, ]
        mock_get_db.return_value.query.return_value.all.return_value = \
            web_site_data
        response = client.get('/api/v1/web-site/')
        mock_get_db.return_value.query.assert_called_once_with(WebSiteModel)
        assert response.status_code == 200
        assert response.get_json() == web_site_data

    @mock.patch('willamette.views.api_v1.web_sites.get_db')
    def test_get(self, mock_get_db, client):
        web_site_key = "36733"
        web_site_data = {
            "_key": web_site_key,
            "inLanguage": "en_us",
            "url": "https://www.vice.com/en_us", }
        mock_get_db.return_value.query.return_value.by_key.return_value = \
            web_site_data
        response = client.get(f'/api/v1/web-site/{web_site_key}/')
        mock_get_db.return_value.query.assert_called_once_with(WebSiteModel)
        mock_get_db.return_value.query.return_value.by_key \
            .assert_called_once_with(web_site_key)
        assert response.status_code == 200
        assert response.get_json() == web_site_data

    @mock.patch('willamette.views.api_v1.web_sites.get_db')
    def test_post(self, mock_get_db, client):
        web_site_data = {
            "inLanguage": "en_us",
            "url": "https://www.vice.com/en_us", }
        db_metadata = {
            "_id": "WebSite/12345",
            "_key": "12345",
            "_rev": "fjhsiz=", }
        # _schema = WebSiteSchema()
        # unmarshal = _schema.load(web_site_data)
        mock_get_db.return_value.add.return_value = db_metadata
        response = client.post('/api/v1/web-site/',
                               data=json.dumps(web_site_data),
                               content_type='application/json')
        # mock_get_db.return_value.add.assert_called_once_with(unmarshal.data)
        assert response.status_code == 201
        assert response.get_json() == db_metadata
