import sys
import matplotlib.pyplot as plt
import os
print(sys.stdout.encoding)
import cv2
img8 = cv2.imread("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\internship-assignment-cv\\Dataset\\img10\\fully_annotated_image.jpg",1)
img8 = cv2.resize(img8, (920, 920))
cv2.imshow("Colored image", img8)
cv2.waitKey(8000)
cv2.destroyAllWindows()

imageLine = img8.copy()
# Draw the image from point A to B
pointA = (0,120)
pointB = (920,920)
cv2.line(imageLine, (0, 120), (920, 920), (255, 255, 0), thickness=3)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(6000)

# make a copy of the original image
imageRectangle = img8.copy()
# define the starting and end points of the rectangle
start_point =(0,120)
end_point =(920,920)
# draw the rectangle
cv2.rectangle(imageRectangle, (0, 120), (920, 920), (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
plt.imshow(imageRectangle[:,:,::-1])
# display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(6000)
# Convert the image to the HSV color space
hsv = cv2.cvtColor(img8, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the red color range
lower_red = (0, 120)
upper_red = (920, 920)

# Create a binary mask for the red regions
mask = cv2.inRange(hsv, (0, 120), (920, 920))


image_path = 'C:\\Users\\Nagendra\\Desktop\\Images folder.py\\imgs\Processed Images'
annotations = [(0, 120), (900, 900)]  # Example annotations (x1, y1, x2, y2)

 #Fill the polygon region with a background color or patch
cv2.fillPoly(img8.jpg, [0, 120, 920, 920], (0, 0, 0))
cv2.imwrite("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\imgs\\Processed Images", img8.jpg)
cv2.imshow('converted image==', img8.jpg)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("output8.png", img8.jpg)
    cv2.waitkey(6000)
    cv2.destroyAllWindows
output_folder = "C:\\Users\\Nagendra\\Desktop\\Images folder.py\\imgs\\Processed Images"
os.makedirs(output_folder, exist_ok=True)
# Assuming you have a list of input images
input_images = ["img8.jpg"]

for image_file in input_images:
    # Load the input image
    image = cv2.imread("output8.png")

    # Perform your image processing operations
    # ...

    # Save the reannotated image into the output folder
cv2.imwrite('output8.png', img8.png)
cv2.waitkey(6000)
cv2.destroyAllWindows


result_image = remove_annotations("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\internship-assignment-cv\\Dataset\img10\\fully_annotated_image.jpg", [(0, 120), (920, 920)])
cv2.imwrite('img8.jpg',result_image)
cv2.waitKey(6000)
cv2.destroyAllWindows()

cv2.imshow("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\internship-assignment-cv\\Dataset\\img10\\fully_annotated_image.jpg", img8.jpg)
cv2.waitKey(8000)
cv2.destroyAllWindows()
