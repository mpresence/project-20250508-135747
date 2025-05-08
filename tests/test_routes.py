def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Calculator' in response.data

def test_calculation_route(client):
    response = client.post('/calculate', data={
        'num1': '5',
        'num2': '3',
        'operation': 'add'
    })
    assert response.status_code == 200
    assert b'8' in response.data
    
    response = client.post('/calculate', data={
        'num1': '10',
        'num2': '2',
        'operation': 'divide'
    })
    assert response.status_code == 200
    assert b'5' in response.data

def test_invalid_input(client):
    response = client.post('/calculate', data={
        'num1': 'abc',
        'num2': '3',
        'operation': 'add'
    })
    assert response.status_code == 200
    assert b'Invalid input' in response.data