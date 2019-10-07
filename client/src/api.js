const API_PATH = process.env && process.env.production
  ? '/api'
  : 'http://127.0.0.1:5000/api'

export async function get_translations() {
  const rawResponse = await fetch(buildApiPath('get_translations'))
  return await rawResponse.json()
}

export async function create_translation(payload) {
  return await do_post('do_translation', payload)
}

export async function check_translation(uid) {
  return await do_post(`check_translation/${uid}`)
}

async function do_post(url, payload) {
  const opts =  {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  }
  if (payload) {
    opts.body =  JSON.stringify(payload)
  }
  const rawResponse = await fetch(buildApiPath(url), opts)
  return rawResponse.json()
}

function buildApiPath(resource) {
  return `${API_PATH}/${resource}`
}