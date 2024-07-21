from marshmallow import Schema, fields


class ProductCreateDtoSchema(Schema):
    product_ids = fields.List(fields.Str(), required=True)


class ProductSchema(Schema):
    id = fields.String()
    product_ids = fields.List(fields.Str())
    total = fields.Float()


class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)