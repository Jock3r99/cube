import imutils
import cv2

def check_contours(frame):
    contours, heira = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_list = list()
    # filter contours

    # loop for checking squaryness
    for c in contours:
        # contour approximation
        perim = cv2.arcLength(c, True)
        # this is cheating lol
        # if perim < 100 or perim > 1000:
        #     continue
        approximation = cv2.approxPolyDP(c, 0.1 * perim, True)
        if len(approximation) == 4:
            # check squaryness
            (x, y, w, h) = cv2.boundingRect(approximation)
            ratio = w / float(h)
            if abs(1-ratio) < 0.05:
                contour_list.append((x, y, w, h))

    # loop to find 9 similarly sized squares
    closeness_factor = .1
    areas_dict = dict()
    for index, c in enumerate(contour_list):
        (x, y, w, h) = c
        areas_dict[index] = w * h
    areas_ordered_tuples = sorted(areas_dict.items(), key=lambda item: item[1])
    print(areas_ordered_tuples)
    for index, area in enumerate(areas_ordered_tuples):
        if index + 8 < len(areas_ordered_tuples):
            small = areas_ordered_tuples[index]
            large = areas_ordered_tuples[index+8]
            if abs(large[1] - small[1]) <= large[1] * closeness_factor:
                final_list = list()
                for item in areas_ordered_tuples[index:index+9]:
                    final_list.append(contour_list[item[0]])
                return final_list

    return []

def draw_contours(frame, contours):
    for index, (x, y, w, h) in enumerate(contours):
        print(contours[index])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

# read in image
image = cv2.imread("images/single_face.png")

# convert to hsv
# hsvimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow("hsv", hsvimage)

# convert to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

# blur
blurred = cv2.blur(gray, (3, 3))
cv2.imshow("blur", blurred)

# canny edge detection
canny = cv2.Canny(blurred, 30, 60, 3)
cv2.imshow("canny", canny)

# dilate with rect structuring element
rect = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
dilated = cv2.dilate(canny, rect)
cv2.imshow("dilated", dilated)

# find contours
contours = check_contours(dilated)
print(len(contours))
draw_contours(image, contours)
cv2.imshow("finished", image)

cv2.waitKey(0)
cv2.destroyAllWindows()