class myDatabase:
    '''
    해싱을 구현합니다
    '''

    def __init__(self, size) :
        '''
        크기 size의 해시 테이블을 만듭니다.

        이곳은 수정하지 마세요.
        '''
        self.myData = [(-1, -1) for i in range(size)]

    def put(self, key, value) :
        '''
        key에 해당하는 값 value 즉, (key, value)를 저장합니다.
        '''
        index = self.hashFunction(key)
        for i in range(len(self.myData)): 
            if self.myData[index][0] == -1: # key가 없는 경우 
                self.myData[index] = (key, value)
                return
            else:
                index = (index + 1) % len(self.myData)
                
    def get(self, key) :
        '''
        key에 해당하는 value를 반환합니다. 만약 key에 해당하는 value가 없다면 -1을 반환합니다.
        '''
        index = self.hashFunction(key)
        for i in range(len(self.myData)):
            if self.myData[index][0] == key: 
                return self.myData[index][1]
                
            #if self.myData[index][0] == -1 :
            #    return -1
                
            index = (index + 1) % len(self.myData)
        return -1 
        
    def hashFunction(self, key) :
        '''
        key에 해당하는 hash 값을 반환합니다.
        '''
        return key % len(self.myData)

def main():
    db = myDatabase(100)

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''
    
    db.put(1, 3)
    db.put(2, 7)
    db.put(3, 8)
    db.put(403, 9)

    print(db.get(3))
    print(db.get(403))


if __name__ == "__main__":
    main()
