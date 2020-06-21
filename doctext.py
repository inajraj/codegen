import argparse
from enum import Enum
import io
import time
import shutil

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
# [END vision_document_text_tutorial_imports]

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_id.json'


class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


BasePath = 'C:/Users/user1/Downloads/HtmlConv/OEBS2701074'
#BasePath = 'C:/Users/user1/Documents/codegen/input'

def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y], None, color)
    return image


def get_document_bounds(image_file, feature):
    # [START vision_document_text_tutorial_detect_bounds]
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    filename = image_file

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    # Collect specified feature bounds by enumerating all document features
    breaks = vision.enums.TextAnnotation.DetectedBreak.BreakType
    paragraphs = []
    lines = []

    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                para = ""
                line = ""
                for word in paragraph.words:
                    for symbol in word.symbols:
                        line += symbol.text
                        if symbol.property.detected_break.type == breaks.SPACE:
                            line += ' '
                        if symbol.property.detected_break.type == breaks.EOL_SURE_SPACE:
                            line += ' '
                            lines.append(line)
                            para += line
                            line = ''
                        if symbol.property.detected_break.type == breaks.LINE_BREAK:
                            lines.append(line)
                            para += line
                            line = ''
                paragraphs.append(para)

    print(paragraphs)
    print(lines)
    outFile = filename[:-3] + "txt"
    processedFiles(lines, outFile)

    # The list `bounds` contains the coordinates of the bounding boxes.
    # [END vision_document_text_tutorial_detect_bounds]
    return bounds
def processedFiles(itemList, filename):
    with open(filename, "w",encoding="utf-8") as f:
        f.write("\n".join(itemList))

def render_doc_text(filein, fileout):
    image = Image.open(filein)
    bounds = get_document_bounds(filein, FeatureType.BLOCK)
    draw_boxes(image, bounds, 'blue')
    bounds = get_document_bounds(filein, FeatureType.PARA)
    draw_boxes(image, bounds, 'red')
    bounds = get_document_bounds(filein, FeatureType.WORD)
    draw_boxes(image, bounds, 'yellow')

    if fileout != 0:
        image.save(fileout)
    else:
        image.show()


if __name__ == '__main__':
    # [START vision_document_text_tutorial_run_application]
    # parser = argparse.ArgumentParser()
    # parser.add_argument('detect_file', help='The image for text detection.')
    # parser.add_argument('-out_file', help='Optional output file', default=0)
    # args = parser.parse_args()

    # render_doc_text(args.detect_file, args.out_file)


    
    #print (BasePath)

    for filename in os.listdir(BasePath):
        if filename.endswith(".jpg"):
            print(filename)
            inputPath = BasePath + '/' + filename
            outputPath = BasePath + '/output/' + filename[:-4]
            get_document_bounds(inputPath, FeatureType.BLOCK)
            shutil.move(BasePath + "/" + filename, BasePath + "/" + "processed")
            shutil.move(BasePath + "/" + filename[:-3] + "txt", BasePath + "/" + "output")
            #time.sleep(1)
    # [END vision_document_text_tutorial_run_application]
# [END vision_document_text_tutorial]