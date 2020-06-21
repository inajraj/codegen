import os
import shutil
import time

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_id.json'

def detect_text(filename, inputPath, outputPath):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    path = inputPath + "/" + filename
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    #get the output filename from path
    outFile = outputPath + "/" + filename.replace('.jpg','.txt')
    for text in texts:
        print('\n"{}"'.format(text.description))
        with open(outFile, 'w',encoding="utf-8") as file:
            file.write(text.description)
        break
        #vertices = (['({},{})'.format(vertex.x, vertex.y)
                    #for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))



def processedFiles(itemList):
    with open("ProcessedFiles.txt", "w") as f:
        f.write("\n".join(itemList))
        


if __name__ == '__main__':

    BasePath = 'C:/Users/User1/Downloads/OEBS2701028'
    inputPath = BasePath 
    outputPath = BasePath + '/output'
    #move the firstfile from basepath to inputpath



    files = []

    files =  open("ProcessedFiles.txt", 'r').read().split('\n')
    #print(files)
    #detect_text('OEBS2701026ws91504.jpg')
    

   
    for filename in os.listdir(BasePath):
        #make sure file does not appear in the list
        
        #if filename not in files:
        if filename.endswith(".jpg"): #and not filename in files:
            print(filename)
            detect_text(filename, BasePath, outputPath)
            #move it to processed foler
            shutil.move(BasePath + "/" + filename, inputPath + "/" + "processed")
            time.sleep(10)
            #files.append(filename)
                #print(filename)
    #processedFiles(files)