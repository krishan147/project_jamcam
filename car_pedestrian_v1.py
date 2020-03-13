# https://stackabuse.com/object-detection-with-imageai-in-python/
# tensorflow version 1.5
from imageai.Detection import ObjectDetection

detector = ObjectDetection()

model_path = "yolo-tiny.h5"
input_path = "./test_images/test3.jpg"
output_path = "./output/newimage.jpg"

detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

for eachItem in detection:

    print (eachItem)

   # print(eachItem["name"] , " : ", eachItem["percentage_probability"])