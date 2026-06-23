import argparse
from models import CopyRequest, PlatformEnum, ToneEnum
from templates import generate_copy_prompt
from generator import generate_copy

def main():
    print("Welcome to my Copywriting Transformer!")
    print("--------------------------------------")
    
    # I used argparse so I can pass arguments from the terminal
    parser = argparse.ArgumentParser(description="Generate marketing copy.")
    parser.add_argument("--name", type=str, required=True, help="Product Name")
    parser.add_argument("--desc", type=str, required=True, help="Product Description")
    parser.add_argument("--platform", type=str, choices=["linkedin", "twitter", "instagram", "email"], required=True)
    parser.add_argument("--tone", type=str, choices=["professional", "casual", "funny", "urgent"], required=True)
    
    args = parser.parse_args()

    try:
        # Pydantic catches errors if the user inputs weird stuff
        req = CopyRequest(
            product_name=args.name,
            product_description=args.desc,
            platform=PlatformEnum(args.platform),
            tone=ToneEnum(args.tone)
        )
    except Exception as e:
        print(f"Validation Error: {e}")
        return

    print("\nGenerating copy... (please wait)")
    
    final_copy = generate_copy(req)
    
    if final_copy:
        print("\n=== FINAL COPY ===")
        print(final_copy)
        print("==================\n")
    else:
        print("\nFailed to generate copy.")

if __name__ == "__main__":
    main()
