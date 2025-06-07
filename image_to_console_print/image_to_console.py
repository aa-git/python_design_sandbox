from PIL import Image
import numpy as np

HORIZONTAL_SKIP_LINES_MODULUS_NUMBER = 3
VERTICAL_SKIP_LINES_MODULUS_NUMBER = 2
BLACK_CHARACTER = '@'

def get_console_matrix_from_image_file(file_name):
    image = Image.open(file_name)
    image = image.convert("RGB")
    pixel_matrix = np.array(image)
    return get_console_matrix_from_numpy_ndarray(pixel_matrix)


def get_console_matrix_from_numpy_ndarray(pixel_matrix):
    matrix = pixel_matrix.tolist()

    #print(type(matrix), len(matrix), type(matrix[0]), type(matrix[0][0]), pixel_matrix.shape)
    x,y,z = pixel_matrix.shape
    console_matrix = [  [0 for j in range(y)] for i in range(x) ]

    def black_pixel(pixel):
        if pixel[0]**2 + pixel[1]**2 + pixel[2]**2 < 15000:
            return True
        return False

    for i in range(x):
        for j in range(y):
            if black_pixel(matrix[i][j]):
                console_matrix[i][j]=0
            else:
                console_matrix[i][j]=1
    return console_matrix



def print_image_on_console(console_matrix):
    skip_counter_vertical=0
    skip_counter_horizontal=0
    
    for row in console_matrix:
        if skip_counter_vertical % VERTICAL_SKIP_LINES_MODULUS_NUMBER==0:
            for cell in row:
                if skip_counter_horizontal % HORIZONTAL_SKIP_LINES_MODULUS_NUMBER == 0:
                    if cell==0:
                        print(BLACK_CHARACTER,end='')
                    else:
                        print(" ", end='')
                skip_counter_horizontal += 1
                
            print("")
        skip_counter_vertical += 1
    return 
    
if __name__ == '__main__':
    print_image_on_console(  get_console_matrix_from_image_file('messi.jpg'))
    

        
