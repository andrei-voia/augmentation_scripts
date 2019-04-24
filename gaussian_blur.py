import os
import cv2


# defined input
FILE_PATH = "C:\\Users\\PREDATOREL\\Desktop\\test"
count_image = 0

print("\nProgram starting...")
print("Opening \"" + str(FILE_PATH) + "\"...")
print("\nFiles:\n")

for filename in os.listdir(FILE_PATH):
    try:
        count_image += 1
        print(filename)
        image = cv2.imread(str(FILE_PATH) + "\\" + str(filename))
        # Gaussian Blurring
        gauss_blur = cv2.GaussianBlur(image, (0, 0), 4)

        cv2.imwrite('C:\\Users\\PREDATOREL\\Desktop\\output\\gaussed_' + str(count_image) + ".png", gauss_blur)

        # cv2.imshow('Gaussian Blurring', gausBlur)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        if count_image > 120:
            break
    except:
        print("Error: \"" + str(filename) + "\" file not recognized as an image format, skipping...")
print("\nEnd of Files...")