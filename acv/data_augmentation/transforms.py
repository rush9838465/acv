import random
import numpy as np
import cv2


class Transformer:

    @staticmethod
    def flip_horizontal(image):
        return cv2.flip(image, 1)

    @staticmethod
    def flip_vertical(image):
        return cv2.flip(image, 0)

    @staticmethod
    def flip_horizontal_vertical(image):
        return cv2.flip(image, -1)

    @staticmethod
    def rotation(image, degrees):
        """
        counter-clockwise direction. rotation with the center.
        """
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, degrees, 1.0)
        return cv2.warpAffine(image, M, (w, h))

    @staticmethod
    def brightness_contrast(image, bt=0., ct=1.):  # 亮度， 对比度
        data = image.astype(np.float)
        data += data * ct + bt
        data = np.clip(data, 0, 255)
        data = data.astype(np.uint8)
        return data

    @staticmethod
    def hsv(image, h, s, v):  # 色彩, 饱和度， 明度
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        img_hsv = img_hsv.astype(np.float)
        if h != 0:
            img_hsv[:, :, 0] += img_hsv[:, :, 0] * h
            img_hsv[:, :, 0] = np.clip(img_hsv[:, :, 0], 0, 180)
        if s != 0:
            img_hsv[:, :, 1] += img_hsv[:, :, 1] * s
            img_hsv[:, :, 1] = np.clip(img_hsv[:, :, 1], 0, 255)
        if v != 0:
            img_hsv[:, :, 2] += img_hsv[:, :, 2] * v
            img_hsv[:, :, 2] = np.clip(img_hsv[:, :, 2], 0, 255)
        img_hsv = img_hsv.astype(np.uint8)
        return cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    @staticmethod
    def crop(image, crop_scale=(0.5, 0.5)):  # 色彩
        """
        :param image: Input image, that need numpy uint8
        :param crop_scale: crop min scale with h,w, max scale is h,w of image
        """
        h, w = image.shape[:2]
        rh = random.randint(int(h * crop_scale[0]), h)
        rw = random.randint(int(w * crop_scale[1]), w)

        offset_x = random.randint(0, w - rw)
        offset_y = random.randint(0, h - rh)
        return image[offset_x:min(offset_x + rw, w - 1), offset_y:min(offset_y + rh, h - 1):]

    @staticmethod
    def blur_gaussian(image, kernel=(3, 3), std=0):
        return cv2.GaussianBlur(image, kernel, std)

    @staticmethod
    def resize_padding(image, dst_hw=(128, 128)):
        """
        :param image: Input image, that need numpy uint8
        :param dst_hw: Target image size h,w
        :return: padding result image
        """
        hs, ws = np.array(dst_hw) / np.array(image.shape[:2])
        img_h, img_w = image.shape[:2]
        if hs < ws:
            align_W, align_H = int(img_w * hs), int(img_h * hs)
        else:
            align_W, align_H = int(img_w * ws), int(img_h * ws)
        img_resized = cv2.resize(image, (align_W, align_H))

        img_paded = np.zeros([dst_hw[0], dst_hw[1], 3], dtype=np.uint8)
        ry, rx = int((dst_hw[0] - align_H) / 2), int((dst_hw[1] - align_W) / 2)
        img_paded[ry:align_H + ry, rx:align_W + rx, :] = img_resized
        return img_paded


if __name__ == '__main__':
    for _ in range(100):
        img = cv2.imread(r'./example.png')
        img1 = Transformer.blur_gaussian(img, [3, 3])
        img1 = Transformer.blur_gaussian(img1, [3, 3])
        img1 = Transformer.blur_gaussian(img1, [3, 3])
        cv2.imshow('ori', img)
        cv2.imshow('result', img1)
        cv2.waitKey(0)
