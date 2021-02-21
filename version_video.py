import cv2
import numpy

def add_ceros(imagerArr):

    for fila in imagerArr:
        fila.insert(0, 160)
        fila.append(160)

    ls = [160] * len(imagerArr[0])

    imagerArr.insert(0, ls)
    imagerArr.append(ls)

    return imagerArr


def binary_to_decimal(lista):
    result = 0
    i = 0
    for bit in reversed(lista):
        result += (2 ** i ) * bit
        i += 1

    return result


def get_new_value(x, y, mat):
    neig = []
    neig.append(mat[x - 1][y - 1])
    neig.append(mat[x - 1][y])
    neig.append(mat[x - 1][y + 1])
    neig.append(mat[x][y - 1])
    neig.append(mat[x][y + 1])
    neig.append(mat[x + 1][y - 1])
    neig.append(mat[x + 1][y])
    neig.append(mat[x + 1][y + 1])

    result = []
    center = mat[x][y]
    for pixel in neig:
        if pixel > center:
            result.append(1)
        else:
            result.append(0)

    return binary_to_decimal(result)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    matriz = frame.tolist()

    census_image = []
    row_temp = []
    for x in range(1, len(matriz) - 1):
        for y in range(1, len(matriz[0]) - 1):
            value = get_new_value(x, y, matriz)
            row_temp.append(value)
        census_image.append(row_temp)
        row_temp = []
    im3 = numpy.array(census_image, dtype=numpy.uint8)

    cv2.imshow('Cambio de color', im3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
