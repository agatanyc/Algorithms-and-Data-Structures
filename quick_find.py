class QuickFind():
    id = []

    def __init__(self, n=None, arr=None):
        if arr == None:
            self.id = self._construct_array(n)
        else:
            self.id = arr

    def _construct_array(self, n):
        temp_arr = []
        for e in range(n):
            temp_arr.append(e)
        return temp_arr

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for e in range(len(self.id)):
            if self.id[e] == pid:
                self.id[e] = qid

if __name__ == '__main__':
    quick_find = QuickFind(10, [])
    print(quick_find)
    print(quick_find._construct_array(10))
