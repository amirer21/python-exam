import hashlib
import json
from BlockChain import Block
from BlockUtil import BlockUtil
import sys, logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')


# 블럭체인 구현 예제에 대한 설명
"""
블록체인은 블록의 연결이다. 블록이 사슬처럼 연결되어 있기 때문에 블록체인이라고 부른다.
첫 번째 블록은 제네시스 블록이라고 부른다. 제네시스 블록은 이전 블록이 없는 블록이다.
두 번째 블록부터는 이전 블록의 해시값을 저장한다. 이전 블록의 해시값을 저장하는 이유는 블록의 무결성을 검증하기 위해서이다.
해시값은 블록의 데이터와 이전 블록의 해시값을 이용하여 계산한다. 블록의 데이터가 변경되면 해시값도 변경된다.
따라서 해시값이 변경되었다는 것은 무결성이 깨졌다는 것을 의미한다.

해시값을 계산하는 알고리즘은 블록체인에서 중요한 역할을 한다. 알고리즘은 SHA256 알고리즘을 사용한다.
SHA256 알고리즘은 블록의 데이터와 이전 블록의 해시값, 난스를 이용하여 해시값을 계산한다.
난스(Nonce)는 해시값을 계산할 때 사용하는 값이다. 난스는 블록의 데이터와 이전 블록의 해시값을 이용하여 계산한다.
난이도는 해시값의 앞자리가 0으로 시작하는 개수를 의미한다. 난이도가 높을수록 해시값을 계산하는데 시간이 오래 걸린다.
어떻게 0을 구하냐면 해시값을 16진수로 변환하여 0이 2개가 나오면 된다.

비트코인 블록체인에서는 이 해시값을 계산하는 알고리즘을 작업증명(Proof of Work)이라고 부른다.
이러한 작업을 마이닝(Mining)이라고 부른다. 마이닝을 하면 새로운 블록이 생성된다. 제일 먼저 해시값을 계산하는 사람이 마이닝(채굴)에 성공한다. 마이닝에 성공하면 비트코인을 보상으로 받을 수 있다.

이 프로젝트 구조를 살펴보자.

BlockChain.py
 - BlockChain 클래스는 블록체인을 구현한 클래스이다.
블록의 데이터는 데이터, 타임스탬프, 이전 해시, 난스 및 해시값이 있다.
- calculate_hash() 메소드는 블록의 해시값을 계산한다. 해시값을 계산할 때는 블록의 데이터, 이전 해시, 난스 및 타임스탬프를 이용한다.
- mine_block() 메소드는 블록을 마이닝한다. 계속 난스를 증가시키면서 해시값을 계산하여 난이도에 맞는 해시값을 찾을 때까지 반복한다.
난스는 0부터 시작하여 1씩 증가시킨다. 난이도는 2로 설정한다. 2가 나온 이유는 0이 2개가 나와야 하기 때문이다.

BlockUtil.py
BlockUtil 클래스는 블록의 해시값을 계산하는 알고리즘을 제공한다.
- apply_sha256() 메소드는 hashlib 모듈의 sha256() 메소드를 사용하여 해시값을 계산한다.
utf-8 인코딩을 사용하여 해시값을 계산한다. hexdigest() 메소드를 사용하여 16진수로 변환한다.
- get_difficulty_string() 메소드는 난이도에 맞는 문자열을 반환한다. 난이도가 2이면 00을 반환한다.

Main.py
Main.py는 블록체인을 생성하고 테스트한다.
 - create_genesis_block() 메소드를 사용하여 제네시스 블록을 생성한다.
 - get_latest_block() 메소드를 사용하여 블록체인의 마지막 블록을 가져온다.
 - add_block() 메소드를 사용하여 블록체인에 블록을 추가한다. 
   add_block()에서는 이전 블록의 해시값을 현재 블록의 previous_hash에 저장한다. 그리고 mine_block() 메소드를 사용하여 블록을 마이닝한다.
 - is_chain_valid() 메소드를 사용하여 블록체인의 유효성을 확인한다.
"""



#class 분리함.
''' Block는 데이터, 이전 해시, 난스 및 해시가 있는 개별 블록 '''
'''
class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[0:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
'''

'''  블록의 체인을 유지하고 제네시스 블록을 생성하고 새 블록을 추가하며 블록체인의 유효성을 확인하는 방법을 제공 '''
class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2 #난이도는 2로 설정.

    def create_genesis_block(self):
        logging.info(sys._getframe(0).f_code.co_name) 
        genesis_block = Block("Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        logging.info(sys._getframe(0).f_code.co_name) 
        return self.chain[-1]

    def add_block(self, new_block):
        logging.info(sys._getframe(0).f_code.co_name) 
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        logging.info(sys._getframe(0).f_code.co_name) 
        target = '0' * self.difficulty
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                print("Current Hashes not equal")
                return False

            if previous_block.hash != current_block.previous_hash:
                print("Previous Hashes not equal")
                return False

            if current_block.hash[:self.difficulty] != target:
                print("This block hasn't been mined")
                return False

        return True


""" 블록체인 생성 및 테스트
    add_block() 메소드를 사용하여 블록체인에 블록을 추가하고, is_chain_valid() 메소드를 사용하여 블록체인의 유효성을 확인
    get_latest_block() 메소드를 사용하여 블록체인의 마지막 블록을 가져옴
    마이닝 되는 블록의 갯수는 총 3개
    난이도는 2 이며, hash 값을 16진수로 변환하여 0이 2개가 나와야 함.
    일치되는 hash 값이 나올 때까지 nonce 값을 증가시키면서 계산하며, 일치되면 마이닝이 완료된 것으로 판단.
    마지막 블록의 hash 값이 다음 블록의 previous_hash 값이 됨.        
"""

if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.create_genesis_block()

    print("Mining block 1... ")
    blockchain.add_block(Block("first block", blockchain.get_latest_block().hash))

    print("Mining block 2... ")
    blockchain.add_block(Block("second block", blockchain.get_latest_block().hash))

    print("Mining block 3... ")
    blockchain.add_block(Block("third block", blockchain.get_latest_block().hash))

    print("\nBlockchain is Valid: " + str(blockchain.is_chain_valid()))

    blockchain_json = json.dumps([block.__dict__ for block in blockchain.chain], indent=4)
    print("\nThe block chain: ")
    print(blockchain_json)
