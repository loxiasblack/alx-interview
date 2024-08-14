#!/usr/bin/python3
""""""


if __name__ == "__main__":
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    

    rotated_array = []
    
    new_line_1 = []
    new_line_1.append(array[2][0])
    new_line_1.append(array[1][0])
    new_line_1.append(array[0][0])
    
    rotated_array.append(new_line_1)
    
    new_line_2 = []
    new_line_2.append(array[2][1])
    new_line_2.append(array[1][1])
    new_line_2.append(array[0][1])
    
    rotated_array.append(new_line_2)
    
    
    new_line_3 = []
    new_line_3.append(array[2][0])
    new_line_3.append(array[1][0])
    new_line_3.append(array[0][0])
    
    
    
    print(f"the array 2D matrice: {array}")
    print("------")
    print(f"the rotated array 90 degree: {rotated_array}")
    
