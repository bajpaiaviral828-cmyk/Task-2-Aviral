import pytest
from models import CopyRequest, PlatformEnum, ToneEnum
from templates import generate_copy_prompt

def test_copy_request_validation():
    req = CopyRequest(
        product_name="Test Product",
        product_description="Test Desc",
        platform="linkedin",
        tone="professional"
    )
    assert req.platform == PlatformEnum.LINKEDIN
    assert req.tone == ToneEnum.PROFESSIONAL

def test_copy_request_invalid_platform():
    with pytest.raises(ValueError):
        CopyRequest(
            product_name="Test Product",
            product_description="Test Desc",
            platform="invalid_platform",
            tone="professional"
        )

def test_generate_copy_prompt_contains_product_info():
    req = CopyRequest(
        product_name="SuperWidget",
        product_description="A widget that is super.",
        platform="email",
        tone="funny"
    )
    prompt = generate_copy_prompt(req)
    
    assert "SuperWidget" in prompt
    assert "A widget that is super." in prompt
    assert "Email" in prompt
    assert "Funny" in prompt
    assert "Subject line" in prompt  # Email platform rule
    assert "Witty and humorous" in prompt  # Funny tone rule
