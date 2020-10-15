import boto3
# import base64
# import json
# import os


recognition_client = boto3.client('rekognition')

image = input('Enter image name along with extension.\n')
file = open(image, 'rb').read()

response = recognition_client.detect_faces(
    Image = {
        'Bytes': file
    }, 
    Attributes=['ALL']
)

for face in response['FaceDetails']:
    print("Gender: {}".format(face['Gender']['Value']))
    print("Age range: {}-{}".format(face['AgeRange']['Low'], face['AgeRange']['High']))
    print("Emotion: {}".format(face['Emotions'][0]['Type']))

    if face['Sunglasses']['Value'] == "true":
        print("The person is wearing sunglasses.")
    else:
        print("The person is not wearing sunglasses.")

    if face['Beard']['Value'] == "true":
        print("The given image is of a person with beard.")
    else:
        print("The person does not have beard.")

    if face['Mustache']['Value'] == "true":
        print("The person has mustache.")
    else:
        print("The person does not have mustache.")