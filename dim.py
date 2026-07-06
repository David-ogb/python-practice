"""
Data Extraction Module

This module provides functions to parse a structured text file containing
column-based data and perform operations on the extracted data.
"""

from typing import Union, Optional, List, Tuple, Dict


def load_data_as_dict(path: str) -> Dict[str, List[str]]:
    """
    Parse a text file and return data as a dictionary.

    The file format consists of columns identified by 'COLUMN' keyword,
    followed by the column name, then data entries, and terminated by 'END'.

    Args:
        path (str): Path to the text file to parse.

    Returns:
        Dict[str, List[str]]: Dictionary with column names as keys and
        lists of entries as values.

    Example:
        >>> load_data_as_dict("data.txt")
        {'Names': ['Fred', 'John', ...], 'Addresses': ['Pontypridd', ...]}
    """
    data_dict = {}
    current_column = None
    current_entries = []

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Check for COLUMN keyword
            if line.upper().startswith('COLUMN '):
                # Save previous column if it exists
                if current_column is not None:
                    data_dict[current_column] = current_entries
                
                # Extract column name (everything after "COLUMN ")
                current_column = line[7:].strip()
                current_entries = []
            
            # Check for END keyword
            elif line.upper() == 'END':
                # Save the last column before ending
                if current_column is not None:
                    data_dict[current_column] = current_entries
                break
            
            # Otherwise, this is a data entry
            else:
                current_entries.append(line)
    
    return data_dict


def load_data_as_list(path: str) -> List[Tuple[str, List[str]]]:
    """
    Parse a text file and return data as a list of tuples.

    The file format consists of columns identified by 'COLUMN' keyword,
    followed by the column name, then data entries, and terminated by 'END'.

    Args:
        path (str): Path to the text file to parse.

    Returns:
        List[Tuple[str, List[str]]]: List of tuples where each tuple contains
        a column name as first element and a list of entries as second element.

    Example:
        >>> load_data_as_list("data.txt")
        [('Names', ['Fred', 'John', ...]), ('Addresses', ['Pontypridd', ...])]
    """
    data_list = []
    current_column = None
    current_entries = []

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Check for COLUMN keyword
            if line.upper().startswith('COLUMN '):
                # Save previous column if it exists
                if current_column is not None:
                    data_list.append((current_column, current_entries))
                
                # Extract column name (everything after "COLUMN ")
                current_column = line[7:].strip()
                current_entries = []
            
            # Check for END keyword
            elif line.upper() == 'END':
                # Save the last column before ending
                if current_column is not None:
                    data_list.append((current_column, current_entries))
                break
            
            # Otherwise, this is a data entry
            else:
                current_entries.append(line)
    
    return data_list


def return_sublist(
    data: Union[Dict[str, List[str]], List[Tuple[str, List[str]]]], 
    col_name: str
) -> Optional[List[str]]:
    """
    Extract the list of entries for a specific column from the data.

    This function works with both dictionary and list formats returned by
    load_data_as_dict() and load_data_as_list().

    Args:
        data: Either a dictionary (str -> List[str]) or a list of tuples
              (str, List[str]) containing the parsed data.
        col_name (str): Name of the column to extract.

    Returns:
        Optional[List[str]]: List of entries for the specified column,
        or None if the column doesn't exist or data format is invalid.

    Example:
        >>> data = load_data_as_dict("data.txt")
        >>> return_sublist(data, "Names")
        ['Fred', 'John', ...]
    """
    # Check if data is a dictionary
    if isinstance(data, dict):
        # Check if column exists
        if col_name in data:
            return data[col_name]
        return None
    
    # Check if data is a list of tuples
    elif isinstance(data, list):
        # Search for the column in the list of tuples
        for column_name, entries in data:
            if column_name == col_name:
                return entries
        return None
    
    # Invalid data type
    else:
        return None


def return_sublist_total(
    data: Union[Dict[str, List[str]], List[Tuple[str, List[str]]]], 
    col_name: str
) -> Optional[float]:
    """
    Calculate the sum of numeric entries in a specific column.

    This function extracts the column entries using return_sublist() and
    attempts to convert each entry to a float. If all entries are numeric,
    it returns their sum. Otherwise, it returns None.

    Args:
        data: Either a dictionary or a list of tuples containing parsed data.
        col_name (str): Name of the column to sum.

    Returns:
        Optional[float]: Sum of all numeric entries in the column,
        or None if the column doesn't exist or contains non-numeric data.

    Example:
        >>> data = load_data_as_dict("data.txt")
        >>> return_sublist_total(data, "Prices")
        442.0
    """
    # Get the column entries using return_sublist
    entries = return_sublist(data, col_name)
    
    # Return None if column doesn't exist
    if entries is None:
        return None
    
    # Try to convert all entries to float
    total = 0.0
    for entry in entries:
        try:
            total += float(entry)
        except (ValueError, TypeError):
            # Entry is not convertible to float
            return None
    
    return total


def return_sublist_mean(
    data: Union[Dict[str, List[str]], List[Tuple[str, List[str]]]], 
    col_name: str
) -> Optional[float]:
    """
    Calculate the mean (average) of numeric entries in a specific column.

    This function extracts the column entries using return_sublist() and
    attempts to convert each entry to a float. If all entries are numeric,
    it returns their mean. Otherwise, it returns None.

    Args:
        data: Either a dictionary or a list of tuples containing parsed data.
        col_name (str): Name of the column to calculate the mean for.

    Returns:
        Optional[float]: Mean of all numeric entries in the column,
        or None if the column doesn't exist or contains non-numeric data.

    Example:
        >>> data = load_data_as_dict("data.txt")
        >>> return_sublist_mean(data, "Prices")
        22.1
    """
    # Get the column entries using return_sublist
    entries = return_sublist(data, col_name)
    
    # Return None if column doesn't exist
    if entries is None:
        return None
    
    # Try to convert all entries to float and calculate mean
    total = 0.0
    count = 0
    
    for entry in entries:
        try:
            total += float(entry)
            count += 1
        except (ValueError, TypeError):
            # Entry is not convertible to float
            return None
    
    # Return None if no entries (shouldn't happen with valid data)
    if count == 0:
        return None
    
    return total / count


def main() -> None:
    """
    Test function to verify the implementation.
    """
    # Test with the provided data files
    print("Testing with Data.txt:")
    print("-" * 50)
    
    # Test load_data_as_dict
    data_dict = load_data_as_dict("Data.txt")
    print("Data loaded as dictionary:")
    for key, values in data_dict.items():
        print(f"  {key}: {len(values)} entries")
    
    print("\nTesting column extraction:")
    names = return_sublist(data_dict, "Names")
    print(f"  Names: {names[:5]}... (showing first 5)")
    
    # Test total and mean for numeric columns
    print("\nTesting with Credit column:")
    total = return_sublist_total(data_dict, "Credit")
    mean = return_sublist_mean(data_dict, "Credit")
    print(f"  Total Credit: {total}")
    print(f"  Mean Credit: {mean}")
    
    print("\nTesting with a non-numeric column:")
    total = return_sublist_total(data_dict, "Addresses")
    print(f"  Total Addresses: {total} (should be None)")
    
    # Test with the sample file
    print("\n" + "=" * 50)
    print("Testing with Sample.txt:")
    print("-" * 50)
    
    data_list = load_data_as_list("Sample.txt")
    print("Data loaded as list of tuples:")
    for col, values in data_list:
        print(f"  {col}: {values}")
    
    # Test return_sublist with list data
    addresses = return_sublist(data_list, "Addresses")
    print(f"\nAddresses: {addresses}")
    
    # Test with non-existent column
    result = return_sublist(data_dict, "NonExistent")
    print(f"Non-existent column: {result} (should be None)")


if __name__ == "__main__":
    main()