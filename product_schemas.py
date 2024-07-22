from marshmallow import Schema, fields


class ProductCreateDtoSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ProductSchema(Schema):
    class Meta:
        fields = ["id", "name", "price"]

    id = fields.Str()
    name = fields.Str()
    price = fields.Float()


class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)