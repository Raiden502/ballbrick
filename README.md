# Ballbrick-Game

- Ballbrick is old school game implemented in python. Allows users to play the game in the command line, It is based on a matrix approach It contains bricks having different powers and balls with a slider that changes its position depending on the ball's position. Users can throw the ball from the slider in different directions like Straight, Right, and Left. The Game can be won when all the bricks get destroyed within the ball count. 

# Conditions
- The game consists power bricks Like DS, DE, B
- If ball hits DS brick, it destroys adjacent bricks in game. 
- If ball hits DE brick, it destroys row containg bricks in game.
- If ball hits B brick, it destroys brick it self and increases the slider length allowing to capture ball easily after its each hit. And ball count won't decreases    allowing user to have extra chance. 
- If ball touches sides of the wall or top of wall with empty bricks reduces ball count only.
- Every hit the slider captures the ball from the position it hits. If the ball hits side walls allows to move freely around the matrix until it hits a brick.
- If every brick destroyed within the ball count The user wins if not the user loses the game

# SOFTWARE REQUIREMENTS:
1. Python 3.6 or above
2. Pycharm or Visual studio code

# INSTRUCTIONS:
1. Open extracted folder name "ballbrick" in editor. 
2. Navigate to the file named "main.py" in root folder which is main file to run the code.
3. Run "main.py" and enter inputs.
4. There is package named game which is a custom package i created and it contains source code for implementations of functions that are used in main file.
   - game package contains "matrixtraverse.py" file indicates implementations of main file.
