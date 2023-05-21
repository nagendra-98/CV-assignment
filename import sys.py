import sys
import matplotlib.pyplot as plt
print(sys.stdout.encoding)
import cv2
img2 = cv2.imread("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\internship-assignment-cv\\Dataset\\1.Sample-img1\\OUTPUT_partially_annotated_image.jpg",1)
img2 = cv2.resize(img2, (900, 900))
cv2.imshow("Colored image", img2)
cv2.waitKey(8000)
cv2.destroyAllWindows()

imageLine = img2.copy()
# Draw the image from point A to B
pointA = (350,350)
pointB = (700, 900)
cv2.line(imageLine, (350, 350), (700, 900), (255, 255, 0), thickness=3)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(6000)

# make a copy of the original image
imageRectangle = img2.copy()
# define the starting and end points of the rectangle
start_point =(350, 350)
end_point =(700, 900)
# draw the rectangle
cv2.rectangle(imageRectangle, (350, 350), (700, 900), (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
plt.imshow(imageRectangle[:,:,::-1])
# display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(6000)
# Convert the image to the HSV color space
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the red color range
lower_red = (350, 350)
upper_red = (700, 900)

# Create a binary mask for the red regions
mask = cv2.inRange(hsv, (350, 350), (700, 900))


image_path = 'C:\\Users\\Nagendra\\Desktop\\Images folder.py\\internship-assignment-cv\Dataset\\1.Sample-img1\\OUTPUT_partially_annotated_image.jpg'
annotations = [(350, 350), (700, 900)]  # Example annotations (x1, y1, x2, y2)

 #Fill the polygon region with a background color or patch
cv2.fillPoly(img2.jpg, [350, 350, 700, 900], (0, 0, 0))
cv2.imwrite("C:\\Users\\Nagendra\Desktop\\Images folder.py\\internship-assignment-cv\\Dataset\\1.Sample-img1\OUTPUT_partially_annotated_image.jpg", img2.jpg)
cv2.imshow('converted image1==', img2.jpg)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("output1.png", img2.jpg)
    cv2.waitkey(6000)
    cv2.destroyAllWindows
output_folder = "C:\\Users\\Nagendra\Desktop\\Images folder.py"
os.makedirs(output_folder, exist_ok=True)
# Assuming you have a list of input images
input_images = ["img2.jpg"]

for image_file in input_images:
    # Load the input image
    image = cv2.imread("output1.png")

    # Perform your image processing operations
    # ...

    # Save the reannotated image into the output folder
cv2.imwrite('output1.png', output1.png)
cv2.waitkey(6000)
cv2.destroyAllWindows


result_image1 = remove_annotations("C:\\Users\\Nagendra\\Desktop\\Images folder.py\\internship-assignment-cv\\Dataset\\1.Sample-img1\OUTPUT_partially_annotated_image.jpg", [(350, 350), (700, 900)])
cv2.imwrite('img2.jpg',result_image1)
cv2.waitKey(6000)
cv2.destroyAllWindows()








