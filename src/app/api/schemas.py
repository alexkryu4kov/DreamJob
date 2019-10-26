from marshmallow import Schema, fields
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class SpecResponseSchema(Schema):
    spec = fields.List(fields.Str(), required=True)


class VacanciesResponseSchema(Schema):
    name = fields.Str(required=True)
    level = fields.Str(required=True)
    salary = fields.Int(required=True)
    skills = fields.List(fields.Str(), required=True)


class SkillsResponseSchema(Schema):
    status = fields.Str(required=True)


class CoursesProfileResponseSchema(Schema):
    url = fields.Str(required=True)
    name = fields.Str(required=True)


class ProfileResponseSchema(Schema):
    known = fields.List(fields.Str(), required=True)
    unknown = fields.List(fields.Str(), required=True)
    courses = fields.List(fields.Nested(CoursesProfileResponseSchema), required=True)
