



export function paginateArray(array: any[], pageNumber: number, pageSize = 4) {
    // Calculate the starting index
    const startIndex = (pageNumber - 1) * pageSize;
    // Slice the array to get the elements for the page
    return array.slice(startIndex, startIndex + pageSize);
  }