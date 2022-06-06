import io
import PIL.Image as Image
from google.cloud import vision


def get_labels(response) -> set:
    labels = [label.description.split() for label in response.label_annotations]
    return {item for sublist in labels for item in sublist}


# This function uses Google API for Vision
def convert_image_to_words(content) -> set[str]:
    image = vision.Image(content=content)
    # Performs label detection on the image file
    client = vision.ImageAnnotatorClient()
    response = client.label_detection(image=image)
    labels = get_labels(response)
    print(f"Labels for this images are {labels}")
    return labels


# MAIN FUNCTION START
def get_words_from_image(image_path):
    # content of URL
    path = r"C:\Users\User\PycharmProjects\projectNLP"
    image = fr"{image_path}"
    full_path = path+image
    image = Image.open(path+image)
    image.save(r'C:\Users\User\PycharmProjects\projectNLP\frontend\static\VIEW5.jpg', 'JPEG')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    words = convert_image_to_words(img_byte_arr)
    return words, full_path
