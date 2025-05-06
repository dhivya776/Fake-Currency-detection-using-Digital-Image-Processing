import cv2

def detect_fake_currency(original_image_path, currency_template_path):
    # Load images
    original_img = cv2.imread(original_image_path)
    currency_template = cv2.imread(currency_template_path)

    # Convert images to grayscale
    original_gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(currency_template, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = new_func(original_gray, template_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Define a threshold for fake currency detection
    threshold = 0.8

    if max_val >= threshold:
        return "There is no fake currency"
    else:
        return "The currency is fake"

def new_func(original_gray, template_gray):
    return cv2.matchTemplate(original_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Example usage:
original_image_path = "D:\DIP-Project\original note.jpg"  # Corrected path
currency_template_path = "D:\DIP-Project\\ake note.jpg"   # Corrected path
new_var = detect_fake_currency(original_image_path, currency_template_path)
result = new_var
print("Result:", result)
