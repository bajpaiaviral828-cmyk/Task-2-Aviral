import csv
import time
from models import CopyRequest
from generator import generate_copy

# I tried to use asyncio here but it was way too complicated.
# So I'm just using a regular for loop with time.sleep() so Google doesn't block my API key.

def process_csv(input_csv_path, output_txt_path):
    print(f"Reading from {input_csv_path}...")
    
    # store the results
    results = []
    
    with open(input_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    print(f"Found {len(rows)} items to process.")
    
    for i, row in enumerate(rows):
        print(f"Processing item {i+1} of {len(rows)}: {row['product_name']}...")
        
        try:
            # using Pydantic here because a tutorial said it's better for catching errors early
            req = CopyRequest(
                product_name=row['product_name'],
                product_description=row['product_description'],
                platform=row['platform'],
                tone=row['tone']
            )
            
            # call gemini
            copy_text = generate_copy(req)
            
            results.append(f"--- Product: {req.product_name} ({req.platform.value} | {req.tone.value}) ---\n{copy_text}\n\n")
            
            # sleep for 3 seconds so we don't hit the free tier rate limit
            # FIXME: maybe make this dynamic later?
            if i < len(rows) - 1:
                time.sleep(3)
                
        except Exception as e:
            print(f"Failed on {row['product_name']}: {e}")
            results.append(f"--- Product: {row['product_name']} [FAILED] ---\nError: {e}\n\n")
            
    # write everything to output file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.writelines(results)
        
    print(f"Done! Saved to {output_txt_path}")
