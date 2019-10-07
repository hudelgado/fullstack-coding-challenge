import json

def request_translation(client, data):
  params = {
    'data': json.dumps(data),
    'content_type': 'application/json'
  }
  return client.post('/api/do_translation', **params)

def test_get_empty_translations(client):
  response = client.get('/api/get_translations')

  assert response.status_code == 200
  assert response.data == b'[]\n'
  assert json.loads(response.data) == []

def test_insert_translation(client):
  initial = {
    'source_language': 'en',
    'target_language': 'es',
    'text': 'Hello world.'
  }
  response = request_translation(client, initial)
  assert response.status_code == 200

  received = json.loads(response.data)
  assert 'uid' in received and received['uid'] is not None
  assert initial['source_language'] == received['source_language']
  assert initial['target_language'] == received['target_language']
  assert initial['text'] == received['text']

def test_duplicated_translation_should_be_te_same(client):
  initial = {
    'source_language': 'en',
    'target_language': 'es',
    'text': 'Hello world.'
  }
  response = request_translation(client, initial)
  assert response.status_code == 200

  received = json.loads(response.data)
  assert 'uid' in received and received['uid'] is not None

  request_translation(client, initial)
  response = request_translation(client, initial)
  assert response.status_code == 200

  second_received = json.loads(response.data)
  assert 'uid' in second_received and second_received['uid'] is not None
  assert received['uid'] == second_received['uid']

def test_check_created_translation_status(client):
  initial = {
    'source_language': 'en',
    'target_language': 'es',
    'text': 'Hello world.'
  }
  response = request_translation(client, initial)
  assert response.status_code == 200

  received = json.loads(response.data)
  assert 'uid' in received and received['uid'] is not None
  assert initial['source_language'] == received['source_language']
  assert initial['target_language'] == received['target_language']
  assert initial['text'] == received['text']

  import time
  time.sleep(60)
  request = client.post('/api/check_translation/{}'.format(received['uid']))
  assert request.status_code == 200

  second_received = json.loads(request.data)
  assert received['uid'] == second_received['uid']
  assert second_received['status'] == 'completed'
  assert second_received['text'] is not None