from marshmallow import Schema, fields
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

spec = APISpec(
    title="Swagger",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)


class SpecResponseSchema(Schema):
    spec = fields.List(fields.Str(), required=True)


class VacancySchema(Schema):
    name = fields.Str(required=True)
    level = fields.Str(required=True)
    company_name = fields.Str(required=True)
    city = fields.Str(required=True)
    salary = fields.Int(required=True)
    skills = fields.List(fields.Str(), required=True)


class VacanciesResponseSchema(Schema):
    vacancies_list = fields.List(fields.Nested(VacancySchema), required = True)


class SkillsResponseSchema(Schema):
    status = fields.Str(required=True)


class CoursesProfileResponseSchema(Schema):
    url = fields.Str(required=True)
    name = fields.Str(required=True)


class ProfileKnownResponseSchema(Schema):
    known = fields.List(fields.Str(), required=True)


class UnknownSchema(Schema):
    name = fields.Str(required=True)
    courses = fields.List(fields.Nested(CoursesProfileResponseSchema), required=True)


class ProfileUnknownResponseSchema(Schema):
    unknown = fields.List(fields.Nested(UnknownSchema), required=True)


spec.components.schema("Spec", schema=SpecResponseSchema)
spec.components.schema("Vacancies", schema=VacanciesResponseSchema)
spec.components.schema("Skills", schema=SkillsResponseSchema)
spec.components.schema("ProfileKnown", schema=ProfileKnownResponseSchema)
spec.components.schema("ProfileUnknown", schema=ProfileUnknownResponseSchema)
print(spec.to_dict())
