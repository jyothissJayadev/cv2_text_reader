import cv2
import cv2.text
import easyocr
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')

# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Read the text from the image
text = reader.readtext(image)

# Set the confidence score threshold
threshold = 0.25

# Loop through detected text
for th in text:
    bbox, text, score = th
    if score > threshold:
        # Draw a rectangle around the text
        top_left = tuple(bbox[0])
        bottom_right = tuple(bbox[2])
        cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 5)
        cv2.putText(image,text,bbox[0],cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)

# Display the image
plt.imshow(cv2.cvtColor(image , cv2.COLOR_BGR2RGB))
plt.show()
