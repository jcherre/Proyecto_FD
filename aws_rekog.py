import boto3
import json
import sys
import os

def detect_labels(photo):
    client = boto3.client('rekognition',
        aws_access_key_id= 'AKIASLLJWUWCZ2KXVYP7',
        aws_secret_access_key= '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'
        )

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    
    data = {
        'source': photo,
        'data': response.get('Labels')
    }
    return json.dumps(data, indent=4)

def find_from_image():
    script = sys.argv[0]

    if len(sys.argv) <= 1:
        print(f'Please supply a file, ex: python3 {script} a1-license.jpg')
        exit(1)
    photo = sys.argv[1]
    print(detect_labels(photo))
    return None


if __name__ == '__main__':
    find_from_image()




