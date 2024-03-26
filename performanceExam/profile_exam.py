import cProfile


class Prime(object):
    """ A prime number iterator for first 'n' primes """

    def __init__(self, n):
        self.n = n
        self.count = 0
        self.value = 0

    # __iter__ : returns an iterator object
    def __iter__(self):
        return self

    # __next__ : returns the next item in the sequence
    def __next__(self):
        """Return next item in iterator """

        if self.count == self.n:
            raise StopIteration("end of iteration")
        return self.compute()

    # 홀수 뿐만 아니라, 짝수도 포함된다.
    # def is_prime(self):
    #     """ Whether current value is prime? """
    #
    #     vroot = int(self.value ** 0.5) + 1
    #     for i in range(3, vroot):
    #         if self.value % i == 0:
    #             return False
    #     return True

    # 홀수만 나누는 것으로 변경해보자.
    def is_prime(self):
        """ Whether current value is prime? """

        vroot = int(self.value ** 0.5) + 1
        # range("start", "stop", "step")
        # range(3, vroot, 2) : 3부터 vroot까지 2씩 증가하는 수열
        for i in range(3, vroot, 2):
            if self.value % i == 0:
                return False
        return True

    def compute(self):
        """ Compute next prime number """

        # Second time, reset value
        if self.count == 1:
            self.value = 1

        while True:
            self.value += 2

            if self.is_prime():
                self.count += 1
                break

        return self.value


def main():
    primes = Prime(1000)
    for p in primes:
        print(p)


if __name__ == "__main__":
    # cProfile을 사용하여 main 함수를 프로파일링
    cProfile.run('main()', filename='prime.stats')

"""
cProfile의 출력은 Python 프로그램 성능에 대한 자세한 정보를 제공합니다. 출력의 각 열이 무엇을 의미하는지 분석해 보겠습니다.

ncalls: 함수 호출 횟수입니다.
tottime: 해당 함수에서 소요된 총 시간입니다(하위 함수 호출에 소요된 시간 제외).
통화당: 통화당 시간입니다. 'tottime'을 'ncalls'로 나눈 몫입니다.
cumtime: 이 기능과 모든 하위 기능(호출부터 종료까지)에서 소요된 누적 시간입니다. 이 수치는 재귀 함수의 경우에도 정확합니다.
percall: 'cumtime'을 기본 호출로 나눈 몫입니다.
filename:lineno(function): 파일 이름, 줄 번호, 함수 이름을 제공합니다.
특정 출력에서:

__init__, __iter__, __next__, is_prime, compute는 Prime 클래스의 메서드입니다. 호출 횟수, 총 시간, 누적 시간과 같은 성능 지표가 제공됩니다.
main 함수가 한 번 호출되어 총(누적) 시간이 0.001초 걸렸습니다.
__next__ 메소드는 11번 호출되었습니다. 이는 10개의 소수를 가져오는 것과 같습니다(__next__에 대한 첫 번째 호출은 반복의 끝을 확인하는 것일 수 있습니다).
is_prime 메소드는 15번 호출되었는데, 이는 각 소수를 계산하는 동안 여러 번 호출되었음을 나타냅니다.
'compute' 메서드는 계산된 각 소수에 대해 한 번씩, 10번 호출되었습니다.
cProfile 출력은 시간이 많이 걸리는 코드 부분을 식별하는 데 도움이 되므로 최적화 후보가 됩니다. 
is_prime 방법이 가장 시간이 많이 걸리는 부분인 것 같습니다. 이는 소수 확인에 계산이 포함되기 때문에 예상됩니다. 
코드를 최적화하려는 경우 is_prime 작동 방식을 살펴보는 것부터 시작해 보세요.

"""