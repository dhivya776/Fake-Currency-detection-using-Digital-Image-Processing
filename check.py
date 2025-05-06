import cv2

# Load original currency image
original_img = cv2.imread("original note.jpg")
cv2.imshow("Original Currency", original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load currency template image
currency_template = cv2.imread("ake note.jpg")
cv2.imshow("Currency Template", currency_template)
cv2.waitKey(0)
cv2.destroyAllWindows()
