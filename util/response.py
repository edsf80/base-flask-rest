from app import ma

class ApiResponse:

    def __init__(self, data):
        self.data = data

class ApiResponseSchema(ma.Schema):
    # Fields to expose
        fields = ("data")

api_response_schema = ApiResponseSchema()