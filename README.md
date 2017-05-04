# project_euler_problem11
Project Euler Problem 11

I run python3 problem11.py

Explanation for calculations algorithm:

I tried to do the least amount of calculations possible. In my algorithm, I made functions that would do products along certain directions. Given two variables, direction1 and direction2, we can go up and down or right and left. They were boolean-like variables. If direction1 was 1 and direction2 was 1, we'd go up and to the right. The rest just follows with combinations of those.

Starting from (0,0), we only need to do calculations to the right, to the right diagonally, and down. Using symmetries like this, I didn't have to do 8 calculations for every number. If we have a 20 x 20 array, I know we only have to calculate the right directions between columns 1 and 16. At columns 17, we only have to calculate the product for column 17 * 18 * 19 * 20, and the respective diagonals to the left. If we are in the range of rows between 1 and 4, we do not have to calculate an up diagonal, so it skips it. Same thing for rows 17 - 20. Kind of tricky, but it cuts the amount calculations by more than half.
