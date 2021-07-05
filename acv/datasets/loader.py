import os
import cv2
from acv.datasets.xml_parsing import VOC as xpVOC
from torch.utils.data import Dataset


class VOC(Dataset):
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
        self.image_type = image_type

        self.xmls = []
        if self.preload2memory:
            print("start load xml files...")
            for one in self.xml_files:
                self.xmls.append(xpVOC.xml2jsonOfbbox(os.path.join(xml_path, one)))
            print("end load!")

    def __getitem__(self, item):
        img = cv2.imread(os.path.join(self.images_path, self.xml_files[item].replace('.xml', self.image_type)))
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
              r'\\10.20.200.170\data\ext\PVDefectData\test2021\zh\dt\VOC2028\JPEGImages',
              preload2memory=False)
    for i, l in voc:
        print(i)
        print(l)
