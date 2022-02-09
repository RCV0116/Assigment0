import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """

        # add your code here
        shape=image_left.shape
        outputImage=np.zeros(shape)

        for i in range(shape [0]):
            for j in range(shape[1]):
                if j in range (column):
                    outputImage[i, j]= image_left[i, j]
                if j in range(column,shape[1]):
                    outputImage[i, j]= image_right[i, j]
        # Please do not change the structure
        return outputImage  # Currently the original image is returned, please replace this with the merged image

    def intensity_scaling(self, input_image, column, alpha, beta):
        outputImage = input_image.copy()
        shape = input_image.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                if j in range(0, column):
                    change = (alpha * outputImage[i, j])
                else:
                    change = (beta * outputImage[i, j])
                if change > 255:
                    change = 255
                if change < 0:
                    change = 0
                outputImage[i, j] = np.uint8(change)
        # Please do not change the structure
        return outputImage  # Currently the input image is returned, please replace this with the intensity scaled image



    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """
        outputImage= input_image.copy()
        shape= input_image.shape
        averageL=0;
        totalL=0;

        averageR=0;
        totalR=0;



        for i in range (shape[0]):
            for j in range(column):
                averageL= averageL + outputImage[i, j]
                totalL= totalL+1

        for i in range(shape[0]):
            for j in range(column, shape[1]):
                averageR = averageR + outputImage[i, j]
                totalR = totalR + 1

        averageL= averageL/totalL
        averageR= averageR/ totalL

        offsetL= 128 - averageL
        offsetR= 128 - averageR

        for i in range(shape[0]):
            for j in range(shape[1]):
                if j in range(0, column):
                    change = (offsetL+ outputImage[i, j])
                else:
                    change = (offsetR + outputImage[i, j])
                if change > 255:
                    change = 255
                if change < 0:
                    change = 0
                outputImage[i, j] = np.uint8(change)

        # add your code here


        return outputImage   # Currently the input image is returned, please replace this with the centralized image
