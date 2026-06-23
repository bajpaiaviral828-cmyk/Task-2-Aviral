from pydantic import BaseModel, field_validator, Field
from typing import Literal
from enum import Enum

# a tutorial on youtube said to use Enums so people can't type random words
class PlatformEnum(str, Enum):
    LINKEDIN = "linkedin"
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    EMAIL = "email"

class ToneEnum(str, Enum):
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    FUNNY = "funny"
    URGENT = "urgent"

class CopyRequest(BaseModel):
    product_name: str
    product_description: str
    # using Pydantic here because string validation manually was getting annoying
    platform: PlatformEnum
    tone: ToneEnum
    temperature: float = 0.9
    top_p: float = 0.95

    @field_validator("temperature")
    @classmethod
    def check_temperature(cls, v):
        if not 0.0 <= v <= 2.0:
            raise ValueError("temperature must be between 0.0 and 2.0")
        return v

    @field_validator("top_p")
    @classmethod
    def check_top_p(cls, v):
        if not 0.0 <= v <= 1.0:
            raise ValueError("top_p must be between 0.0 and 1.0")
        return v

    @field_validator("product_name", "product_desc")
    @classmethod
    def not_empty(cls, v):
        if not v.strip():
            raise ValueError("field cannot be empty")
        return v.strip()


class CopyOutput(BaseModel):
    platform: str
    tone: str
    product_name: str
    temperature: float
    top_p: float
    copy_text: str
