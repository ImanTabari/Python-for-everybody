'''
Create a function called sort_matrix that takes a multidimensional array which represents a square matrix, as a parameter, 
and returns a same n x n sized matrix in which the elements are sorted in ascending order. 
(for sorting you can use the built in sort or sorted list method)
'''

def sort_matrix(matrix):
    Matrixsize = len(matrix)
    OneDimensionList = []
    SortedMatrix = []
    
    for i in range(Matrixsize):
        for j in range(Matrixsize):
            OneDimensionList.append(matrix[i][j])
    OneDimensionList.sort()
    while len(OneDimensionList) > 0:
        InnerSortedList = []
        for Index in range(Matrixsize):
            InnerSortedList.append(OneDimensionList.pop(0))
        SortedMatrix.append(InnerSortedList)
    return SortedMatrix

UnsortedMatrix = [[4,2,3],[2,1,7],[7,2,6]]

smatrix = sort_matrix(UnsortedMatrix)
for element in smatrix:
    print(element)

                
