# Skyscrapers Solver
- This script solves Puzzle "Daily Skyscrapers" on [BrainBashers:Skyscrapers](https://www.brainbashers.com/skyscrapers.asp) using backtracking
- The rule of this puzzle can be found here: [Skyscrapers Help](https://www.brainbashers.com/skyscrapershelp.asp)

Example of a Skyscrapers problem (9x9):

![image](https://user-images.githubusercontent.com/39042628/64927104-59bb5a80-d7d4-11e9-8b81-6dd6c0f79c9c.png)

Input can be entered as follows:

![image](https://user-images.githubusercontent.com/39042628/64927119-7b1c4680-d7d4-11e9-959b-80441f240375.png)

Answer will be displayed in the command line similar to this:

![image](https://user-images.githubusercontent.com/39042628/64927145-de0ddd80-d7d4-11e9-9fa5-f438dff9f386.png)

Correct cells are marked Green and incorrect cells are marked Red on BrainBashers. This can be used to check the correctness of the algorithm

![image](https://user-images.githubusercontent.com/39042628/64927161-12819980-d7d5-11e9-9868-6312fb41eb6c.png)

#### Limitation:
Because of nature of backtracking, problems with missing condition similar to the following increases number of guesses exponentially. This problem can be fixed by pre-populating a pool of guesses for each cell before running. For example, `Cell(row = 7, col = 8)`'s value must be`9` because of the condition `1` to the right. 

Furthermore, pool of values is also restricted by the surrounding conditions. For example, in col 6, `6` on top means that:
 - `9` cannot be in any of the first 5 rows 
 - `8` cannot be in any of the first 4 rows
 - `7` cannot be in any of the first 3 rows
 - `6` cannot be in any of the first 2 rows
 - `5` cannot be in the first row 

![image](https://user-images.githubusercontent.com/39042628/64927210-c08d4380-d7d5-11e9-9738-85dfbb0b75e0.png)

#### Future features:
- Pre-populate a pool of values for each cell based on top, bot, left, right
- Use Image recognition to automatically get matrix instead of manually entering the value
- Give url link to the problem and script can put in answer
