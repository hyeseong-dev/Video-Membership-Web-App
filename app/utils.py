import json
from app.users import schemas

from pydantic import BaseModel, error_wrappers
from pydantic.error_wrappers import ValidationError


def valid_schema_data_or_error(raw_data: dict, SchemaModel: BaseModel):
    data = {}
    errors = []
    error_str = None
    try:
        cleaned_data = schemas.UserSignupSchema(**raw_data)
        data = cleaned_data.dict()
        if error_str is not None:
            pass
    except error_wrappers.ValidationError as e:
        error_str = e.json()
        errors = json.loads(error_str)
    except Exception as e:
        errors = [{"loc": "non_field_error", "msg": "Unknown error"}]
    return data, errors