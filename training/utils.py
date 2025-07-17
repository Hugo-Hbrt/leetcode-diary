import re
import unicodedata

def slugify(text):
    # Normalize Unicode characters (e.g. é → e)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    
    # Lowercase the string
    text = text.lower()
    
    # Replace spaces and hyphens with underscores
    text = re.sub(r'[\s\-]+', '_', text)
    
    # Remove all non-word characters except underscores
    text = re.sub(r'[^\w_]', '', text)
    
    # Remove leading/trailing underscores
    text = text.strip('_')
    
    return text
