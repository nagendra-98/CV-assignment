import sys
import matplotlib.pyplot as plt
import os
print(sys.stdout.encoding)
import cv2
img3 = cv2.imread("C:\\Users\\Nagendra\\Desktop\Images folder.py\\internship-assignment-cv\\Dataset\\2.Sample-img2\\fully_annotated_image.jpg",1)
img3 = cv2.resize(img3, (900, 900))
cv2.imshow("Colored image", img3)
cv2.waitKey(8000)
cv2.destroyAllWindows()

imageLine = img3.copy()
# Draw the image from point A to B
pointA = (0,120)
pointB = (900,900)
cv2.line(imageLine, (0, 120), (900, 900), (255, 255, 0), thickness=3)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(6000)

# make a copy of the original image
imageRectangle = img3.copy()
# define the starting and end points of the rectangle
start_point =(0,120)
end_point =(900,900)
# draw the rectangle
cv2.rectangle(imageRectangle, (0, 120), (900, 900), (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
plt.imshow(imageRectangle[:,:,::-1])
# display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(6000)
# Convert the image to the HSV color space
hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the red color range
lower_red = (0, 120)
upper_red = (900, 900)

# Create a binary mask for the red regions
mask = cv2.inRange(hsv, (0, 120), (900, 900))


image_path = 'C:\\Users\\Nagendra\\Desktop\\Images folder.py\\imgs\Processed Images'
annotations = [(0, 120), (900, 900)]  # Example annotations (x1, y1, x2, y2)

 #Fill the polygon region with a background color or patch
cv2.fillPoly(img3.jpg, [0, 120, 900, 900], (0, 0, 0))
cv2.imwrite("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\imgs\\Processed Images", img3.jpg)
cv2.imshow('converted image==', img3.jpg)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("output.png", img3.jpg)
    cv2.waitkey(6000)
    cv2.destroyAllWindows
output_folder = "C:\\Users\\Nagendra\\Desktop\\Images folder.py\\imgs\\Processed Images"
os.makedirs(output_folder, exist_ok=True)
# Assuming you have a list of input images
input_images = ["img3.jpg"]

for image_file in input_images:
    # Load the input image
    image = cv2.imread("output3.png")

    # Perform your image processing operations
    # ...

    # Save the reannotated image into the output folder
cv2.imwrite('output3.png', img3.png)
cv2.waitkey(6000)
cv2.destroyAllWindows


result_image = remove_annotations("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\internship-assignment-cv\\Dataset\\2.Sample-img2\\fully_annotated_image.jpg", [(0, 120), (900, 900)])
cv2.imwrite('img3.jpg',result_image)
cv2.waitKey(6000)
cv2.destroyAllWindows()
