# Cleaning Steps 

1. Visually inspect all the images and delete the one which seems not like table
2. Remove all the corresponding xml files by running the script:
    - Python3 remove_xml.py
3. Generate statistics of all image and save in csv file
    - Percentage of Spanning
    - No. of rows
    - No. of columns
    - Total no. of cells
    - Aspect ratio
    - Width_added 
    - Height_added
    - Is_complex
4. Create the new square image by adding padding either top/bottom or right/left depending upon the aspect ratio. 
5. Perform EDA on the percentage of spanning cell
6. Perform EDA for rows counts
7. Perform EDA for column counts
8. Perform EDA for aspect ratio
9. Perform EDA for complex and simple
10. Draw bounding boxes for train images & square train images
11. Summary Stats


