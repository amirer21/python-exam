import hashlib
import time
import logging, sys
from BlockUtil import BlockUtil

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')

''' Block는 데이터, 이전 해시, 난스 및 해시가 있는 개별 블록 '''
class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = int(time.time())
        self.nonce = 0
        self.hash = self.calculate_hash()

    ''' 블록의 해시를 계산 '''
    def calculate_hash(self):
        sha = hashlib.sha256() # sha256 해시 알고리즘 사용
        sha.update( # sha256 해시 알고리즘에 데이터를 넣어서 해시를 계산
            str(self.previous_hash).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.nonce).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8')
        )
        return sha.hexdigest() # 해시를 16진수로 변환하여 반환

    ''' 블록을 채굴 '''
    def mine_block(self, difficulty):
        logging.info(sys._getframe(0).f_code.co_name) 
        #target = '0' * difficulty
        #String target = BlockUtil.getDifficultyString(difficulty);
        target = BlockUtil.get_difficulty_string(difficulty)
        
        ## todo : 난스를 증가시키고 해시를 계산하여 난이도에 맞는 해시를 찾을 때까지 반복
        ## 난이도는 2로 설정. 2가 나온 이유는 0이 2개가 나와야 하기 때문.
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            print("nonce:", self.nonce, "difficulty:", target, "hash:", self.hash)
        print("Block Mined!!!:", self.hash)

'''
if __name__ == '__main__':
    block = Block("first block", "0")
    block.mine_block(2)
'''