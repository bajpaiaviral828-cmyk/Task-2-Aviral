# this is the master prompt that controls the AI
BASE_PROMPT = """You are an expert copywriter. Your task is to write high-converting copy based on the constraints below.

PRODUCT:
Name: {product_name}
Description: {product_desc}

PLATFORM RULES:
You are writing for: {platform}
{platform_rules}

TONE RULES:
The tone should be: {tone}
{tone_rules}

Please output ONLY the requested copy. No yapping or intros.
"""

def get_platform_rules(platform):
    # specific rules for each platform so it doesn't sound the same everywhere
    rules = {
        "linkedin": "- Keep it professional but engaging.\n- Use a hook in the first line.\n- End with a question to drive comments.",
        "instagram": "- Highly visual language.\n- Short, punchy sentences.\n- Include exactly 3 relevant hashtags.",
        "email": "- Must include an eye-catching Subject Line.\n- Break text into short paragraphs.\n- Clear Call-to-Action (CTA) button at the bottom."
    }
    return rules.get(platform.lower(), "- Write standard marketing copy.")

def get_tone_rules(tone):
    # changing how it sounds
    rules = {
        "professional": "- Authoritative and trustworthy.\n- No slang.",
        "casual": "- Write like you are texting a friend.\n- Very relaxed.",
        "funny": "- Witty and humorous.\n- Don't take it too seriously.",
        "inspirational": "- Uplifting and motivating.\n- Focus on the big picture.",
        "urgent": "- Create a strong sense of FOMO (Fear Of Missing Out).\n- Push for immediate action."
    }
    return rules.get(tone.lower(), "- Write in a neutral tone.")

def generate_copy_prompt(req):
    # fill in the f-string variables with my rules
    return BASE_PROMPT.format(
        product_name=req.product_name,
        product_desc=req.product_description,
        platform=req.platform.value.upper(),
        platform_rules=get_platform_rules(req.platform.value),
        tone=req.tone.value.upper(),
        tone_rules=get_tone_rules(req.tone.value)
    )
