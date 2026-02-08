from pydantic import BaseModel, Field, ConfigDict
from pydantic_core import core_schema
from datetime import datetime
from bson import ObjectId
from typing import Optional, Any

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, __source_type: Any, __handler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(
            function=cls.validate,
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def validate(cls, v: str) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, __core_schema: core_schema.CoreSchema, __handler
    ):
        return __handler(core_schema.str_schema())

class CommonModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
