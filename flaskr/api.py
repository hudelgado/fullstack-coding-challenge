from flask import Blueprint, jsonify, request
from peewee import fn
import json

from unbabel.api import UnbabelApi

api_bp = Blueprint('api', __name__, url_prefix='/api', static_folder="../www")
from translator.models import Translation, NEW_STATUS, PENDING_STATUS, DONE_STATUS

# end point to perform translations
@api_bp.route('/do_translation', methods=['POST'])
def do_translation():
  data = json.loads(request.data)
  try:
    translation = (
      Translation
      .select()
      .where(
        Translation.source_language == data['source_language'],
        Translation.target_language == data['target_language'],
        Translation.text == data['text']
      )
    ).get()
  except Translation.DoesNotExist:
    job = create_translation_job(data)
    job_status = 'requested' if job.status == 'new' else job.status
    translation = Translation.create(uid=job.uid, status=job_status, **data)

  return jsonify(translation.to_dict())

# end point to retrieve all translations
@api_bp.route('/get_translations', methods=['GET'])
def get_translations():
  translations = [translation.to_dict() for translation in (Translation
    .select()
    .order_by(fn.length(Translation.text).desc())
  )]
  return jsonify(translations)

STATUS_MAPPING = {
  'new': NEW_STATUS,
  'translating': PENDING_STATUS,
  'completed': DONE_STATUS,
}

# end point update a translation
@api_bp.route('/check_translation/<uid>', methods=['POST'])
def get_translation(uid):
  translation = Translation.select().where(Translation.uid == uid).get()
  if translation.status != DONE_STATUS:
    update_translation_from_job(translation)
  return jsonify(translation.to_dict())

def create_translation_job(data):
  from .config import API_USERNAME, API_KEY, TEST_API
  uapi = UnbabelApi(API_USERNAME, API_KEY, sandbox=TEST_API)
  return uapi.post_translations(**data)

def update_translation_from_job(translation):
  from .config import API_USERNAME, API_KEY, TEST_API
  uapi = UnbabelApi(API_USERNAME, API_KEY, sandbox=TEST_API)
  updated = uapi.get_translation(translation.uid)

  if translation.status == STATUS_MAPPING[updated.status]:
    return False

  if STATUS_MAPPING[updated.status] == DONE_STATUS:
    translation.translation = updated.translation
    translation.status = updated.status
  else:
    translation.status = updated.status

  translation.save()
  return True