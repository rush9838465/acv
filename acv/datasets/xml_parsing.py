import os
import cv2
from lxml import etree


class VOC:
    @staticmethod
    def xml2jsonOfbbox(file_path, label_care=None):
        """
        :param file_path: xml files path
        :return: json results
        """
        anno = []
        xl = etree.parse(file_path)
        root = xl.getroot()
        # file_name = root.find('filename').text
        objects = root.findall('object')
        for ob in objects:
            one_annotation = {}
            label = ob.find('name').text
            if label_care:
                if label not in label_care:
                    continue
            one_annotation['tag'] = label
            one_annotation['flag'] = False
            bbox = ob.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)
            one_annotation['bbox'] = [xmin, ymin, xmax, ymax]
            anno.append(one_annotation)
        return anno

    @staticmethod
    def get_iou_from_xml(files_path, images_path, label_care=[''], debug=True, img_type='.jpg'):
        """
        :param file_path: xml files path
        :return: save files to ./iou_results
        """
        xmls = os.listdir(files_path)

        for one in xmls:
            if not one.endswith('.xml'):
                continue
            xl = etree.parse(os.path.join(files_path, one))
            root = xl.getroot()
            objects = root.findall('object')
            img = cv2.imread(os.path.join(images_path, one.replace('.xml', img_type)),)
            if not os.path.exists('./iou_results'):
                os.mkdir("./iou_results")

            for idx, ob in enumerate(objects):
                one_annotation = {}
                label = ob.find('name').text
                if label not in label_care:
                    continue
                one_annotation['tag'] = label
                one_annotation['flag'] = False
                bbox = ob.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)
                cv2.imwrite(f"./iou_results/{one[:-4]}_{idx}.jpg", img[ymin:ymax, xmin:xmax])
                if debug:
                    print(f"./iou_results/{one[:-4]}_{idx}.jpg: ", idx)


if __name__ == '__main__':
    VOC.get_iou_from_xml(r'C:\Users\98384\Desktop\Desktop',
                         r'C:\Users\98384\Desktop\Desktop',
                         label_care=['HDPY'],
                         debug=True,
                         img_type='.jpg')
