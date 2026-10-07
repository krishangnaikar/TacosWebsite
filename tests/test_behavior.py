import app

def test_home_and_menu_are_available():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    assert client.get('/').status_code == 200
    response = client.get('/menu')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    for section in app.MENU:
        assert section['id'] in html
        for column in section['columns']:
            for item in column['items']:
                assert item['name'] in html

def test_menu_anchors_are_unique():
    ids = [section['id'] for section in app.MENU]
    assert len(ids) == len(set(ids))

def test_missing_page_and_unsupported_method():
    client = app.app.test_client()
    assert client.get('/missing').status_code == 404
    assert client.post('/menu').status_code == 405
