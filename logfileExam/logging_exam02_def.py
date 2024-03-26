### log 세팅
import logging
import time

def get_logger(name=None):
    # 1 logger instance를 만듭니다.
    logger = logging.getLogger(name)

    # 2 logger의 level을 가장 낮은 수준인 DEBUG로 설정합니다.
    logger.setLevel(logging.DEBUG)

    # 3 formatter 지정하여 log head를 구성해줍니다.
    ## asctime - 시간정보
    ## levelname - logging level
    ## funcName - log가 기록된 함수
    ## lineno - log가 기록된 line
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s")

    # 4 handler instance 생성하여 console 및 파일로 저장할 수 있도록 합니다. 파일명은 txt도 됩니다.
    console = logging.StreamHandler()
    #now date time
    now = time.localtime()
    filename = "log_" + str(now.tm_year) + str(now.tm_mon) + str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min) + str(now.tm_sec)
    file_handler_debug = logging.FileHandler(filename=f"{filename}_debug.log", encoding='utf-8') # encoding='utf-8' 추가
    file_handler_error = logging.FileHandler(filename=f"{filename}_error.log", encoding='utf-8') # encoding='utf-8' 추가

    # 5 handler 별로 다른 level 설정합니다. 설정한 level 이하 모두 출력,저장됩니다.
    console.setLevel(logging.INFO) # console에는 info 이상만 출력
    file_handler_debug.setLevel(logging.DEBUG) # debug 이상 파일에 저장
    file_handler_error.setLevel(logging.ERROR)

    # 6 handler 출력을 format 지정방식으로 합니다.
    console.setFormatter(formatter)
    file_handler_debug.setFormatter(formatter)
    file_handler_error.setFormatter(formatter)

    # 7 logger에 handler 추가합니다.
    logger.addHandler(console)
    logger.addHandler(file_handler_debug)
    logger.addHandler(file_handler_error)

    # 8 설정된 log setting을	반환합니다.
    return logger


def main():
    logger = get_logger(__name__)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

def example_function():
    try:
        # Your code here
        result = 10 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Log the error along with the traceback
        #logging.error("An error occurred: %s", str(e), exc_info=True)
        #get_logger(__name__).error("An error occurred: %s", str(e), exc_info=True)
        print("An error occurred: %s", str(e), exc_info=True)
    
if __name__ == "__main__":
    main()
    example_function()
    
    
    
    