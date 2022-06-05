import numpy
import cv2

"""
This code gets a path for image and return the encoded message in it.
"""


def decode_img(path: str) -> str:
    """
    this function gets a path for image and return the encoded message in it.
    :param path: path to picture
    :return: the encoded message
    """
    img = cv2.imread (path, 0)
    stacked_arr = numpy.column_stack (numpy.where (img == 1))
    coords = sorted (stacked_arr, key=lambda x: x[1])
    return "".join ([chr (row) for row, col in coords])


if __name__ == '__main__':
    msg = decode_img ('code.png')
    print (msg)