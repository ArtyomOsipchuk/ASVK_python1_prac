class Maze:
    def __init__(self, n):
        self.n = n
        self.N = n * 2 + 1
        self.maze = [["█" for i in range(self.N)] for j in range(self.N)]
        for i in range(n):
            for j in range(n):
                self.maze[i * 2 + 1][j * 2 + 1] = "·"

    def __str__(self):
        s = []
        for i in range(self.N):
            row = ''
            for j in range(self.N):
                row += self.maze[j][i]
            s.append(row)
        return '\n'.join(s)

    def __getitem__(self, exp):
        y0, slic, x1 = exp
        x0, y1 = slic.start, slic.stop
        x0, y0, y1, x1 = x0 * 2 + 1, y0 * 2 + 1, y1 * 2 + 1, x1 * 2 + 1
        scout = [[0 for i in range(self.N)] for j in range(self.N)]
        scout[y0][x0] = 1
        flag = True
        while flag:
            flag = False
            for i in range(self.N):
                for j in range(self.N):
                    if scout[j][i] == 1:
                        for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            ia = i + a
                            jb = j + b
                            if 0 <= ia < self.N and 0 <= jb < self.N:
                                if scout[jb][ia] == 0 and self.maze[jb][ia] == '·':
                                    scout[jb][ia] += 1
                                    if jb == y1 and ia == x1:
                                        continue
                                    flag = True
        return bool(scout[y1][x1])

    def __setitem__(self, exp, val):
        y0, slic, x1 = exp
        x0, y1 = slic.start, slic.stop
        if x0 == x1:
            y0, y1 = min(y0, y1), max(y0, y1)
            for i in range(y0 * 2 + 1, y1 * 2 + 1):
                self.maze[i][x0 * 2 + 1] = val
        if y0 == y1:
            x0, x1 = min(x0, x1), max(x0, x1)
            for i in range(x0 * 2 + 1, x1 * 2 + 1):
                self.maze[y0 * 2 + 1][i] = val


import sys

exec(sys.stdin.read())
