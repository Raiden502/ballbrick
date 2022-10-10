# i have created custom package contains codes to calculate and run the model
class gamemodels_initialization:

    # initialize global values
    def __init__(self, matrix, total_size, extended_slider, score):
        self.matrix = matrix
        self.total_size = total_size
        self.extended_slider = extended_slider
        self.score = score

    # create matrix
    def create_matrix(self, size):
        for i in range(size):
            for j in range(size):
                if i == 0 or j == 0 or j == size - 1:
                    self.matrix[i][j] = "w"
                elif i == size - 1 and j > 0 and j != int(i / 2) and j < size - 1:
                    self.matrix[i][j] = "G"
        self.matrix[size-1][int((size-1)/2)] = "o"
        return self.matrix

    # create input based matrix
    def input_matrix(self, i, j, k):
        if i == self.total_size - 1 or j == self.total_size - 1 or i == 0 or j == 0:
            raise Exception(
                "entered coordinates out of boundaries: (values should exists in range of" + " 0 and " + str(
                    self.total_size - 1) + ")")
        else:
            self.matrix[i][j] = k
            return

    # return values to main
    def getvalues(self):
        return self.matrix

    # update slider position
    def update_slider_loc(self, i):
        f = self.matrix[-1].index("o")
        self.matrix[-1][f], self.matrix[-1][i] = self.matrix[-1][i], self.matrix[-1][f]
        
    # returns current position of ball at ground level
    def current_pos(self):
        k = self.matrix[-1].index("o")
        return self.total_size - 1, k

    # converts string to int and leaves character
    def check_alpha(self, c):
        try:
            c = int(c)
            return c
        except ValueError:
            return c

    # checks all values are zero or not
    def check_scoreboard(self):
        flag = False
        for i in range(1, self.total_size - 1):
            for j in range(1, self.total_size - 1):
                if self.matrix[i][j] == 0:
                    flag = True
                else:
                    return False
        return flag

    # make row zeros
    def blast_row(self, index_x):
        for i in range(1, self.total_size - 1):
            self.matrix[index_x][i] = 0
        return

    # make adjacent values zeros
    def blast_adjacent(self, index_x, index_y):
        # top
        if index_x == 1 and index_y > 1 and index_x < self.total_size - 1:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y + 1] = 0
            self.matrix[index_x][index_y - 1] = 0
            self.matrix[index_x + 1][index_y - 1] = 0
            self.matrix[index_x + 1][index_y + 1] = 0
            return
        # top left
        elif index_x == 1 and index_y == 1:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y + 1] = 0
            self.matrix[index_x + 1][index_y + 1] = 0
            return
        # top right
        elif index_x == 1 and index_y == self.total_size - 2:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y - 1] = 0
            self.matrix[index_x + 1][index_y - 1] = 0
            return
        # left
        elif index_y == 1 and 1 < index_x < self.total_size - 1:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y + 1] = 0
            self.matrix[index_x + 1][index_y + 1] = 0
            self.matrix[index_x - 1][index_y] = 0
            self.matrix[index_x - 1][index_y + 1] = 0
            return
        # right
        elif index_y == self.total_size - 2 and 1 < index_x < self.total_size - 1:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y - 1] = 0
            self.matrix[index_x + 1][index_y - 1] = 0
            self.matrix[index_x - 1][index_y] = 0
            self.matrix[index_x - 1][index_y - 1] = 0
            return
        # down
        elif index_x == self.total_size - 2 and 1 < index_y < self.total_size - 1:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y + 1] = 0
            self.matrix[index_x][index_y - 1] = 0
            self.matrix[index_x - 1][index_y - 1] = 0
            self.matrix[index_x - 1][index_y + 1] = 0
            self.matrix[index_x - 1][index_y] = 0
            return
        # down left
        elif index_x == self.total_size - 2 and index_y == 1:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y + 1] = 0
            self.matrix[index_x - 1][index_y + 1] = 0
            self.matrix[index_x - 1][index_y] = 0
            return
        # down right
        elif index_x == self.total_size - 2 and index_y == self.total_size - 2:
            self.matrix[index_x][index_y] = 0
            self.matrix[index_x][index_y - 1] = 0
            self.matrix[index_x - 1][index_y - 1] = 0
            self.matrix[index_x - 1][index_y] = 0
            return
        # middle
        elif 1 < index_x < self.total_size - 1 and 1 < index_y < self.total_size - 1:
            self.matrix[index_x][index_y + 1] = 0
            self.matrix[index_x][index_y - 1] = 0
            self.matrix[index_x - 1][index_y - 1] = 0
            self.matrix[index_x - 1][index_y + 1] = 0
            self.matrix[index_x - 1][index_y] = 0
            self.matrix[index_x + 1][index_y - 1] = 0
            self.matrix[index_x + 1][index_y + 1] = 0
            self.matrix[index_x][index_y] = 0
            return

    # Straight hit from ground level
    def straight_ball(self, ball_i, ball_j):
        # if ball touches to upper wall
        if ball_i < 1:
            self.score -= 1
            return self.score
        
        # if ball hits a brick
        elif self.matrix[ball_i][ball_j] != 0 and self.matrix[ball_i][ball_j] != "DE" and self.matrix[ball_i][
            ball_j] != "DS" and self.matrix[ball_i][ball_j] != "B":
            self.matrix[ball_i][ball_j] -= 1
            self.score -= 1
            return self.score

        # if ball hits a brick value DE
        elif self.matrix[ball_i][ball_j] == "DE":
            gamemodels_initialization.blast_row(self, ball_i)
            self.score -= 1
            return self.score
        
        # if ball hits a brick value DS
        elif self.matrix[ball_i][ball_j] == "DS":
            gamemodels_initialization.blast_adjacent(self, ball_i, ball_j)
            self.score -= 1
            return self.score

        # if ball hits a brick value B
        elif self.matrix[ball_i][ball_j] == "B":
            self.extended_slider += 1
            self.matrix[ball_i][ball_j] = 0
            ii, jj = gamemodels_initialization.current_pos(self)
            if self.extended_slider % 2 != 0:
                if jj != self.total_size - 2:
                    self.matrix[ii][jj + 1] = "-"
            else:
                if jj != 1:
                    self.matrix[ii][jj - 1] = "-"
            return self.score

        else:
            return gamemodels_initialization.straight_ball(self, ball_i - 1, ball_j)

    # right from ground level
    def right_diagnol(self, ball_i, ball_j, k):

        # if ball touches upper wall
        if ball_i < 1:
            self.score -= 1
            return self.score
        
        # if ball hits the right side wall
        if ball_j == self.total_size - 1:
            
            # traversing the horizontal path
            for i in range(self.total_size - 1, 0, -1):
                
                # checking for a brick
                if str(self.matrix[ball_i][i]).isdigit() and self.matrix[ball_i][i] > 0:
                    self.matrix[ball_i][i] -= 1
                    gamemodels_initialization.update_slider_loc(self, i)
                    self.score -= 1
                    return self.score

                # if ball hits a brick value DE
                elif self.matrix[ball_i][i] == "DE":
                    gamemodels_initialization.blast_row(self, ball_i)
                    gamemodels_initialization.update_slider_loc(self, i)
                    self.score -= 1
                    return self.score

                # if ball hits a brick value DS
                elif self.matrix[ball_i][i] == "DS":
                    gamemodels_initialization.blast_adjacent(self, ball_i, i)
                    gamemodels_initialization.update_slider_loc(self, i)
                    self.score -= 1
                    return self.score
                
                # if ball hits a brick value B
                elif self.matrix[ball_i][ball_j] == "B":
                    self.extended_slider += 1
                    self.matrix[ball_i][ball_j] = 0
                    ii, jj = gamemodels_initialization.current_pos(self)
                    if self.extended_slider % 2 != 0:
                        if jj != self.total_size - 2:
                            self.matrix[ii][jj + 1] = "-"
                    else:
                        if jj != 1:
                            self.matrix[ii][jj - 1] = "-"
                    return self.score
                
            else:
                gamemodels_initialization.update_slider_loc(self, int(self.total_size / 2))
                self.score -= 1
                return self.score

        # if ball hits a brick
        elif self.matrix[ball_i][ball_j] != 0 and self.matrix[ball_i][ball_j] != "DE" and self.matrix[ball_i][
            ball_j] != "DS" and self.matrix[ball_i][ball_j] != "B":
            self.matrix[ball_i][ball_j] -= 1
            gamemodels_initialization.update_slider_loc(self, ball_j)
            self.score -= 1
            return self.score

        # if ball hits a brick value DE
        elif self.matrix[ball_i][ball_j] == "DE":
            gamemodels_initialization.blast_row(self, ball_i)
            gamemodels_initialization.update_slider_loc(self, ball_j)
            self.score -= 1
            return self.score

        # if ball hits a brick value DS
        elif self.matrix[ball_i][ball_j] == "DS":
            gamemodels_initialization.blast_adjacent(self, ball_i, ball_j)
            gamemodels_initialization.update_slider_loc(self, ball_j)
            self.score -= 1
            return self.score

        # if ball hits a brick value B
        elif self.matrix[ball_i][ball_j] == "B":
            self.extended_slider += 1
            self.matrix[ball_i][ball_j] = 0
            ii, jj = gamemodels_initialization.current_pos(self)
            if self.extended_slider % 2 != 0:
                if jj != self.total_size - 2:
                    self.matrix[ii][jj + 1] = "-"
            else:
                if jj != 1:
                    self.matrix[ii][jj - 1] = "-"
            return self.score

        else:
            return gamemodels_initialization.right_diagnol(self, ball_i - 1, ball_j + k, k)

    # left hit from ground level
    def left_diagnol(self, ball_i, ball_j, k):

        # if ball hits upper wall
        if ball_i < 1:
            self.score -= 1
            return self.score

        # if ball hits the left side wall
        if ball_j == 0:

            # traversing the horizontal path
            for i in range(1, self.total_size - 1):

                # checking for a brick
                if str(self.matrix[ball_i][i]).isdigit() and self.matrix[ball_i][i] > 0:
                    self.matrix[ball_i][i] -= 1
                    gamemodels_initialization.update_slider_loc(self, i)
                    self.score -= 1
                    return self.score

                # if ball hits a brick value DE
                elif self.matrix[ball_i][i] == "DE":
                    gamemodels_initialization.blast_row(self, ball_i)
                    gamemodels_initialization.update_slider_loc(self, i)
                    self.score -= 1
                    return self.score

                # if ball hits a brick value DS
                elif self.matrix[ball_i][i] == "DS":
                    gamemodels_initialization.blast_adjacent(self, ball_i, i)
                    gamemodels_initialization.update_slider_loc(self, i)
                    self.score -= 1
                    return self.score

                # if ball hits a brick value B
                elif self.matrix[ball_i][ball_j] == "B":
                    self.extended_slider += 1
                    self.matrix[ball_i][ball_j] = 0
                    ii, jj = gamemodels_initialization.current_pos(self)
                    if self.extended_slider % 2 != 0:
                        if jj != self.total_size - 2:
                            self.matrix[ii][jj + 1] = "-"
                    else:
                        if jj != 1:
                            self.matrix[ii][jj - 1] = "-"
                    return self.score

            else:
                gamemodels_initialization.update_slider_loc(self, int(self.total_size / 2))
                self.score -= 1
                return self.score

        # if ball hits a brick
        elif self.matrix[ball_i][ball_j] != 0 and self.matrix[ball_i][ball_j] != "DE" and self.matrix[ball_i][
            ball_j] != "DS" and self.matrix[ball_i][ball_j] != "B":
            self.matrix[ball_i][ball_j] -= 1
            gamemodels_initialization.update_slider_loc(self, ball_j)
            self.score -= 1
            return self.score

        # if ball hits a brick value DE
        elif self.matrix[ball_i][ball_j] == "DE":
            gamemodels_initialization.blast_row(self, ball_i)
            gamemodels_initialization.update_slider_loc(self, ball_j)
            self.score -= 1
            return self.score

        # if ball hits a brick value DS
        elif self.matrix[ball_i][ball_j] == "DS":
            gamemodels_initialization.blast_adjacent(self, ball_i, ball_j)
            gamemodels_initialization.update_slider_loc(self, ball_j)
            self.score -= 1
            return self.score

        # if ball hits a brick value B
        elif self.matrix[ball_i][ball_j] == "B":
            self.extended_slider += 1
            self.matrix[ball_i][ball_j] = 0
            ii, jj = gamemodels_initialization.current_pos(self)
            if self.extended_slider % 2 != 0:
                if jj != self.total_size - 2:
                    self.matrix[ii][jj + 1] = "-"
            else:
                if jj != 1:
                    self.matrix[ii][jj - 1] = "-"
            return self.score

        else:
            return gamemodels_initialization.left_diagnol(self, ball_i - 1, ball_j + k, k)
