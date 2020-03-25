# https://stackabuse.com/object-detection-with-imageai-in-python/
# tensorflow version 1.5
from imageai.Detection import ObjectDetection
from os import listdir
from os.path import isfile, join

detector = ObjectDetection()

model_path = "yolo-tiny.h5"
input_path = "./test_images/"
output_path = "./output/newimage.jpg"


onlyfiles = [f for f in listdir(input_path) if isfile(join(input_path, f))]

print (onlyfiles)


for f in onlyfiles:
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()
    detection = detector.detectObjectsFromImage(input_image=input_path+f, output_image_path="./output/result"+f)

    for eachItem in detection:

        print (eachItem)

       # print(eachItem["name"] , " : ", eachItem["percentage_probability"])