import hashlib
import json
import logging, sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')

class BlockUtil:
    ''' 블록의 해시를 계산 '''
    @staticmethod
    def apply_sha256(input):
        logging.info(sys._getframe(0).f_code.co_name) 
        try:
            digest = hashlib.sha256() 
            digest.update(input.encode('utf-8'))
            hash = digest.hexdigest() 
            return hash
        except Exception as e:
            raise RuntimeError(e)

    ''' json 문자열로 변환 '''
    @staticmethod
    def get_json(o):
        return json.dumps(o, sort_keys=True, indent=4) #sort_keys=True : key를 정렬하여 반환, indent=4 : 들여쓰기 4칸

    ''' 난이도에 맞는 문자열을 반환 '''
    @staticmethod
    def get_difficulty_string(difficulty):        
        logging.info('%s [difficulty] :: %s', sys._getframe(0).f_code.co_name, str(difficulty))
        return '0' * difficulty

'''
if __name__ == '__main__':
    input_str = "example"
    hash = BlockUtil.apply_sha256(input_str)
    print("Hash:", hash)

    object_to_serialize = {"data": "example", "timestamp": 1234567890}
    json_string = BlockUtil.get_json(object_to_serialize)
    print("JSON:", json_string)

    difficulty_string = BlockUtil.get_difficulty_string(2)
    print("Difficulty String:", difficulty_string)
'''