import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def convert_to_black_white(image_path):

    img = Image.open(image_path)
    img_gray = img.convert('L')
    
    img_matrix = list(img_gray.getdata())
    width, height = img_gray.size
    img_matrix = [img_matrix[i * width:(i + 1) * width] for i in range(height)]
    
    return img_matrix

def display_bw_image(image_matrix):

    plt.imshow(image_matrix, cmap='gray')
    plt.axis('off')  # Hides the axes
    plt.title("Original Image")
    plt.show()

def display_bw_image_svd(image_matrix, k_value):

    plt.imshow(image_matrix, cmap='gray')
    plt.axis('off')  # Hides the axes
    plt.title(f"SVD Image for K: {k_value}")
    # plt.savefig(f"./assets/reconstructed_images/image_{k_value}")
    # plt.show()

if __name__ == '__main__':

    image_path = './assets/image.png'  
    bw_matrix = convert_to_black_white(image_path)
    bw_matrix = np.array(bw_matrix)

    print(bw_matrix)  
    print(f'Image dimensions: {len(bw_matrix[0])} x {len(bw_matrix)}')

    display_bw_image(bw_matrix)

    for i in range(15):
        k_value = ((i//2)**2+i+1)*(i+1)
        reconstructed_image = apply_svd_to_image(bw_matrix, k_value)
        display_bw_image_svd(reconstructed_image, k_value)

