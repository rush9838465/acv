import numpy as np
import cv2


def resize_padding(img, dst_hw=[64, 164]):
    """
    :param img: Input image, that need numpy uint8
    :param dst_hw: Target image size
    :return: padding result image
    """
    hs, ws = np.array(dst_hw) / np.array(img.shape[:2])
    img_h, img_w = img.shape[:2]
    if hs < ws:
        align_W, align_H = int(img_w * hs), int(img_h * hs)
    else:
        align_W, align_H = int(img_w * ws), int(img_h * ws)
    img_resized = cv2.resize(img, (align_W, align_H))

    img_paded = np.zeros([dst_hw[0], dst_hw[1], 3], dtype=np.uint8)
    ry, rx = int((dst_hw[0] - align_H) / 2), int((dst_hw[1] - align_W) / 2)
    img_paded[ry:align_H + ry, rx:align_W + rx, :] = img_resized
    return img_paded

