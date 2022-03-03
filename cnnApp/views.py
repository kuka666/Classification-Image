from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import tensorflow-cpu as tf
import json
from tensorflow-cpu import Graph
from PIL import Image , ImageOps
import numpy as np
from .models import imagepostgre

class_name = ["airplane", "automobile" , "bird" , "cat" , "deer" , "dog" , "frog" , "horse" , "ship" , "truck"]

def load_my_model():
    model = tf.keras.models.load_model("./models/my_model.h5")
    return model

model = load_my_model()

# Create a title of web App


# create a file uploader and take a image as an jpg or png
# file = st.file_uploader("Upload the image" , type=["jpg" , "png"])

def predictImage(request):
    print (request)
    print (request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)

    testimage='.'+filePathName
    img1 = image.load_img(testimage)
    # x = image.img_to_array(img)
    # x=x/255
    # x=x.reshape(1,img_height, img_width,3)

    # with model_graph.as_default():
    #     with tf_session.as_default():
    #         predi=model.predict(x)

    predictedLabel=import_and_predict(img1)

    context={'filePathName':filePathName,'predictedLabel':predictedLabel}
    a = imagepostgre(name=predictedLabel, link=filePathName)
    a.save()
    return render(request,'index.html',context)

# Create a function to take and image and predict the class
def import_and_predict(img1):
    size = (32,32)
    image = ImageOps.fit(img1, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    predict = class_name[np.argmax(prediction)]
    return predict

# if st.button("Predict"):
#     image = Image.open(file)
#     st.image(image , use_column_width=True)
#     predictions = import_and_predict(image , model)
#
#     class_name = ["airplane", "automobile" , "bird" , "cat" , "deer" , "dog" , "frog" , "horse" , "ship" , "truck"]
#
#     string = "Image mostly same as :-" + class_name[np.argmax(predictions)]
#     st.success(string)





# model_graph = Graph()
# with model_graph.as_default():
#     tf_session = tf.compat.v1.Session()
#     with tf_session.as_default():
#         model = load_model('./models/MobileNetModelImagenet.h5')


def index(request):
    context={'a':1}
    return render(request,'index.html',context)



# def predictImage(request):
#     print (request)
#     print (request.POST.dict())
#     fileObj=request.FILES['filePath']
#     fs=FileSystemStorage()
#     filePathName=fs.save(fileObj.name,fileObj)
#     filePathName=fs.url(filePathName)
#     testimage='.'+filePathName
#     img = image.load_img(testimage, target_size=(img_height, img_width))
#     x = image.img_to_array(img)
#     x=x/255
#     x=x.reshape(1,img_height, img_width,3)
#     with model_graph.as_default():
#         with tf_session.as_default():
#             predi=model.predict(x)
#
#     import numpy as np
#     predictedLabel=labelInfo[str(np.argmax(predi[0]))]
#
#     context={'filePathName':filePathName,'predictedLabel':predictedLabel[1]}
#     return render(request,'index.html',context)

# def viewDataBase(request):
#     import os
#     listOfImages=os.listdir('./media/')
#     listOfImagesPath=['./media/'+i for i in listOfImages]
#     context={'listOfImagesPath':listOfImagesPath}
#     return render(request,'viewDB.html',context)
