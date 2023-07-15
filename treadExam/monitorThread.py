import threading
import time

#Thread 클래스
class TossMonitorThread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval
        #self._stop = threading.Event()
        self._stop_event = threading.Event()
        #_stop_event는 스레드가 중지되어야 하는지 계속 실행되어야 하는지 신호를 보내는데 사용된다.
        self.terminate_flag = True

    def run(self):
        while self.terminate_flag:
            if self.stopped():
                print("stopped")
                return			
            print("주기적으로 실행")
            time.sleep(self.interval)
    
    def stop(self):
        #self._stop.set()
        self._stop_event.set()
        #특정 이벤트가 발생했음을 나타내는 이벤트를 설정하는 데 사용된다.
        #내부 플래그를 true로 설정한다.
        
    def stopped(self):
        #return self._stop.is_set()
        return self._stop_event.is_set()
        #내부 플래그가 true인 경우에만 true를 반환한다.
        #is_set은 _stop_event설정되어 있으면 스레드가 중지되고 run()메서드가 루프를 종료하고 반환해야 함을 의미합

    def terminate(self):
        self.terminate_flag = False

#Toast Error Monitor 클래스
class ToastErrorMonitor:
    def toastMonitor(self):
        returnErrorText = ''
        while True:            
            try:
                #(1) error 토스 클래스(notification-title) 가져오기            
                returnText = DEV1.UIGetObject(fieldName='class', fieldValue='notification-title', occurrence=0)                
                #(2) error 토스 클래스가 있다면, 해당 클래스, 텍스트가 맞는지 확인
                if returnText[1].viewClassName == "notification-title" and returnText[1].text == "ERROR":
                    #(3) 에러 텍스트 출력하기(notification-message클래스의 text)
                    returnErrorText = DEV1.UIGetObject(fieldName='class', fieldValue='notification-message', occurrence=0)
                    print('[Toast Error Found] text :: ', returnErrorText[1].text)
                    #(4) 테스트 결과를 "Failed"로 설정하고, 테스트 종료
                    System.Finish(T_FAILED, "Failed")                                
            except Exception as e:
                print('not found toast error')                                
            
            if returnErrorText == 'Error':            
                print("Exiting the thread...")
                monitor_thread.terminate()  # Set the termination flag
                monitor_thread.join()  # Wait for the thread to finish
                break
            else:
                print("Toast Error Not Found")
            time.sleep(3)  # Sleep for 3 seconds
        print("---Toast Error monitor 종료---")
        
#Monitor 실행
monitor_thread = TossMonitorThread(interval=3)  # 매 2초마다 반복하여 모니터링
monitor_thread.start()

#쓰레드 중지
time.sleep(10)
monitor_thread.stop()
monitor_thread.join()