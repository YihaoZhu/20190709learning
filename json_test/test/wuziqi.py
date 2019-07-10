import random

class wuziqi:
    def __init__(self,num):
        #初始化棋盘
        self.qipan = [[0]*num]*num
        #黑方下一步棋
        self.black = 1
        #白方下一步棋
        self.white = -1
        #打平局
        self.sign = 0
        #跑函数
        self.play()
        self.flag = random.choice([self.black,self.white])

    def play(self):
        #标志位记录是否棋盘下完
        over = 1
        #选择某一行
        row = int(input("Please choose a row num:"))
        #选择某一列
        column = int(input("Please choose a column num:"))
        #判断谁先下第一步
        if self.flag == 1:
            self.qipan[row][column] = 1
            self.flag -= 2
        else:
            self.qipan[row][column] = -1
            self.flag += 2
        for i in range(len(self.qipan[0])):
            for j in range(len(self.qipan[1])):
                if self.qipan[i][j] == 0:
                    over = 0
                    break
        if not over:
            self.who_win()
            self.play()

    def who_win(self):
        black_score_row = 0
        white_score_row = 0
        black_score_column = 0
        white_score_column = 0
        black_score_diag = 0
        white_score_diag = 0
        black_score_inverse_diag = 0
        white_score_inverse_diag = 0
        #判断行列：
        #self.sign为2时，黑棋赢
        #self.sign为1时，白棋赢
        for i in range(len(self.qipan[0])):
            for j in range(len(self.qipan[1])):
                if self.qipan[i][j] == 1:
                    black_score_column += 1
                elif self.qipan[i][j] == -1:
                    white_score_column += 1
                if self.qipan[j][i] == 1:
                    black_score_row += 1
                elif self.qipan[j][i] == -1:
                    white_score_row += 1
            if black_score_column >= 5 | black_score_row >=5:
                self.sign += 2
                self.winner()
                break

            elif white_score_column >= 5 | white_score_row >=5:
                self.sign -= 2
                self.winner()
                break
        self.sign = 0
        #判断对角线
        for k in range(len(self.qipan[0])):
            if self.qipan[k][k] == 1:
                black_score_diag += 1
            elif self.qipan[k][k] == -1:
                white_score_diag += 1
            if self.qipan[k][len(self.qipan[0])-1-k] == 1:
                black_score_inverse_diag += 1
            elif self.qipan[k][len(self.qipan[0])-1-k] == -1:
                white_score_inverse_diag += 1
        if black_score_inverse_diag >= 5:
            self.sign += 2
            self.winner()
        elif white_score_inverse_diag >= 5:
            self.sign -= 2
            self.winner()

    def winner(self):
        if self.sign == 2:
            print("black win")
        elif self.sign == -2:
            print("white win")
        else:
            print("Tie Game")


wuziqi(10)
