import os
image_dir = "train_images"
xml_dir = "train_label"

images = [img.split('.')[0] for img in os.listdir(image_dir)]
xmls = [xml.split('.')[0] for xml in os.listdir(xml_dir)]


for remove_xml in list(set(xmls) - set(images)):
    try:
        xml_filename = xml_dir+ "/" + remove_xml + ".xml"
        os.remove(xml_filename)
        print(xml_filename)
    except:
        pass