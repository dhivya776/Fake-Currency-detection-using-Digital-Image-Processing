import cv2
import numpy as np

def detect_currency(original_currency_path, currency1_path, currency2_path):
    original_currency = cv2.imread(original_currency_path, cv2.IMREAD_GRAYSCALE)
    currency1 = cv2.imread(currency1_path, cv2.IMREAD_GRAYSCALE)
    currency2 = cv2.imread(currency2_path, cv2.IMREAD_GRAYSCALE)

    res1 = cv2.matchTemplate(original_currency, currency1, cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(original_currency, currency2, cv2.TM_CCOEFF_NORMED)

    max_corr1 = np.max(res1)
    max_corr2 = np.max(res2)

    if max_corr1 > max_corr2:
        print("Currency 2 is fake.")

    elif max_corr2 > max_corr1:
        print("Currency 1 is fake.")
        
    else:
        print("Both currencies are equally similar to each other")

detect_currency("images/original_currency.jpg", "images/currency1.jpg", "images/currency2.jpg")
