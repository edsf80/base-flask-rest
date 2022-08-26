from app import app
from jsonschema import ValidationError
from flask import make_response, jsonify

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        print(original_error.path)
        return make_response(jsonify({'error': original_error.message}), 400)    
    return error