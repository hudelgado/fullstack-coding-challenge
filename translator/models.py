from peewee import Field, CharField, TextField, UUIDField, SQL
from playhouse.shortcuts import model_to_dict
import json

from .db import db_wrapper

NEW_STATUS = 'requested'
PENDING_STATUS = 'pending'
DONE_STATUS = 'translated'

class EnumField(Field):
  db_field = "enum"

  def pre_field_create(self, model):
    field = "e_%s" % self.name

    self.get_database().get_conn().cursor().execute(
      "DROP TYPE IF EXISTS %s;" % field
    )

    query = self.get_database().get_conn().cursor()

    tail = ', '.join(["'%s'"] * len(self.choices)) % tuple(self.choices)
    q = "CREATE TYPE %s AS ENUM (%s);" % (field, tail)
    query.execute(q)

  def post_field_create(self, model):
    self.db_field = "e_%s" % self.name

  def coerce(self, value):
    if value not in self.choices:
      raise Exception("Invalid Enum Value `%s`", value)
    return str(value)

  def get_column_type(self):
    return "enum"

  def __ddl_column__(self, ctype):
    return SQL("e_%s" % self.name)

class Translation(db_wrapper.Model):
  """Data model for a translation

  Attributes
  ----------
  source_language : CharField
    Source language of the translation
  target_language : CharField
    Destination language of the translation
  text : TextField
    The text to be translated
  translation : TextField
    The computed translation
  status : EnumField
    The status of the current translation
     - values: requested, pending or translated
  """

  source_language = CharField()
  target_language = CharField()
  text = TextField()
  translation = TextField(null=True)
  status = EnumField(default=NEW_STATUS, choices=[NEW_STATUS, PENDING_STATUS, DONE_STATUS])
  uid = CharField()

  def __str__(self):
    """Get the string representation of the model"""
    return json.dumps(self.to_dict())

  def to_dict(self):
    return model_to_dict(self)

  class Meta:
    indexes = (
      (('source_language', 'target_language', 'text'), True),
      SQL('CREATE INDEX translation_length_sentence ON translation(LENGTH(text))'),
    )
    only_save_dirty = True