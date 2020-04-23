from pprint import pprint

bigmap = {'0':[], '1': [[1]],
          '2': [[1, 1], [0, 1]],
          '3': [[1, 1, 1], [0, 0, 1], [1, 1, 1]],
          '4': [ [1, 1, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 1, 1, 1]
               ],
          '5': [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1],
                [1, 1, 1, 0, 1], [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]],
          '8': [[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]
          }


def spiralize(size=5):
    if str(size) in bigmap:
        return bigmap[str(size)]
    else:

        maps = [[0] * size for _ in range(size)]
        for row in range(size):
            for col in range(size):
                if row == 0:
                    maps[row][col] = 1
                elif row == size-1:
                    maps[row][col] = 1
                elif col == size - 1:
                    maps[row][col] = 1
                elif col == 0 and row > 1:
                    maps[row][col] = 1
        maps[2][1] = 1
        small_map = spiralize(size-4)
        # pprint(maps)
        for row in range(2, size-2):
            for col in range(2, size-2):
                maps[row][col] = small_map[row-2][col-2]

        #pprint(maps, indent=10)
        bigmap[str(size)] = maps
        return maps
