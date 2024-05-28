from PIL import Image
import sys
import datetime
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def get_image_metadata(image_path):
    """
    Extracts metadata from an image file.
    """
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        
        if exif_data is not None:
            for tag_id in exif_data:
                tag = TAGS.get(tag_id, tag_id)
                data = exif_data.get(tag_id)
                
                # Convert datetime objects to readable string
                if isinstance(data, datetime.datetime):
                    data = data.strftime('%Y:%m:%d %H:%M:%S')
                
                print(f"{tag}: {data}")
        else:
            print("No EXIF data found.")
            
    except IOError:
        print(f"Unable to open image file: {image_path}")

def main():
    """
    Main function to handle command-line arguments and call get_image_metadata.
    """
    if len(sys.argv) < 2:
        print("Usage: python scorpion.py FILE1 [FILE2...]")
        return
    
    for file_path in sys.argv[1:]:
        print(f"\nMetadata for {file_path}:\n")
        get_image_metadata(file_path)

if __name__ == "__main__":
    main()
