class ArvoreFewick:
    def init(self, N):
        self.__n = N
        self.__BIT = [0 for i in range(N + 1)]

    def update(self, i, x):
        j = i

        while j <= self.__n:
            self.__BIT[j] += x
            j += (j & -j)

    def query(self, l, r):
        return self.__get_sum(r) - self.__get_sum(l - 1)

    def __get_sum(self, i):
        sum, j = i

        while j > 0:
            sum += self.__BIT[j]
            j -= j & -j

        return sum
