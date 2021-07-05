import os
import cv2
from .xml_parsing import VOC as xpVOC


class VOC:
    def __init__(self, xml_path, images_path, preprocess=None, preload2memory=True, image_type='.jpg'):
        """
        :param xml_path: xml files path.
        :param images_path: image files path.
        :param preprocess: preprocess function hook,
         that need 2 parameters image(result from cv2.imread()) and label({'tag':'cat', 'bbox':[xmin, ymin, xmax, ymax]}).
        :param preload2memory: preload xml files to memory.
        :param image_type: dataset images type.
        """
        self.xml_path = xml_path
        self.images_path = images_path
        self.xml_files = os.listdir(xml_path)
        # self.images_files = os.listdir(images_path)
        self.preload2memory = preload2memory
        self.preprocess = preprocess
        self.images_path = image_type

        self.xmls = []
        if self.preload2memory:
            for one in self.xml_files:
                self.xmls.append(xpVOC.xml2jsonOfbbox(os.path.join(xml_path, one)))

    def __getitem__(self, item):
        img = cv2.imread(os.path.join(self.images_path, self.xml_files[item].replace('.xml', self.images_path)))
        if self.preload2memory:
            label = self.xmls[item]
        else:
            label = xpVOC.xml2jsonOfbbox(os.path.join(self.xml_path, self.xml_files[item]))
        if self.preprocess:
            img, label = self.preprocess(img, label)
        return img, label

    def __len__(self):
        return len(self.xml_files)


if __name__ == '__main__':
    voc = VOC(r'\\10.20.200.170\data\ext\PVDefectData\test2021\zh\dt\VOC2028\Annotations',
                  r'\\10.20.200.170\data\ext\PVDefectData\test2021\zh\dt\VOC2028\JPEGImages',)


