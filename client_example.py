import requests
import sys

def extract_doc(file_path, api_url="http://127.0.0.1:8000/extract"):
    """
    Sends a file to the docling-extractor API and prints the result.
    """
    try:
        print(f"Sending {file_path} to {api_url}...")
        
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(api_url, files=files)
        
        if response.status_code == 200:
            data = response.json()
            print("\n--- Markdown Content (First 1000 chars) ---")
            print(data.get("markdown")[:1000] + "...\n")
            
            print("Extraction Successful!")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"Failed to request: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client_example.py <path_to_document>")
    else:
        file_path = sys.argv[1]
        extract_doc(file_path)
