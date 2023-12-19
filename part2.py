from importer import *

def part2():

    frobenius = {}

    image_path = './assets/image.png'  
    bw_matrix = convert_to_black_white(image_path)
    bw_matrix = np.array(bw_matrix)

    print(bw_matrix)  
    print(f'Image dimensions: {len(bw_matrix[0])} x {len(bw_matrix)}')

    display_bw_image(bw_matrix)

    for i in range(50):
        k_value = (i+1)*20
        reconstructed_image = apply_svd_to_image(bw_matrix, k_value)
        # display_bw_image_svd(reconstructed_image, k_value)

        frobenius[k_value] = frobenius_norm(bw_matrix-reconstructed_image)

    plot_dict_as_graph(frobenius, "K Values", "Frobenius", "Frobenius by K Values")
