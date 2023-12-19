import numpy as np
import matplotlib.pyplot as plt

def apply_svd_to_image(image_matrix, k):
    U, S, Vt = np.linalg.svd(image_matrix, full_matrices=False)
    reconstructed_image = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))
    
    return reconstructed_image

def frobenius_norm(matrix):
    return np.linalg.norm(matrix, 'fro')
