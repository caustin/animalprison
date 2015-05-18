from marshmallow import Schema, fields


class Service(Schema):
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    location = fields.Url(required=True)

    def make_object(self, data):
        return Service(**data)
