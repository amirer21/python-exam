<h2 id="ossystem-vs-subprocess"  data-ke-size="size26">os.system vs subprocess</h2>
<p  data-ke-size="size16">Linux(ubuntu)의 shell scirpt 파일을 실행하여야 하고자 한다. 파이썬의 시스템 명령어 실행 라이브러리 비교하였다.</p>
<h3 id="1-ossystem"  data-ke-size="size23">1. os.system</h3>
<p  data-ke-size="size16"><b>(1) os.system</b><span>&nbsp;</span>:단순하게 명령 실행을 위해 사용할 때는 적합하다.</p>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="clean"><code>import os
    #os.system()
    os.system ('python test.py') # 파이썬 실행
</code></pre>
</div>
</div>
<p  data-ke-size="size16"><b>(2) os.popen</b><span>&nbsp;</span>: 실행 결과값을 변수에 저장하려면 다음과 같이 사용한다.</p>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="lua"><code>    os.popen('shell 실행 명령어')
</code></pre>
</div>
</div>
<p  data-ke-size="size16"><b>(3) os.read</b><span>&nbsp;</span>: 실행 결과를 출력하고 싶다면, read()를 사용한다.</p>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="lua"><code>    os.popen('shell 실행 명령어').read()
</code></pre>
</div>
</div>
<h3 id="2-subprocess"  data-ke-size="size23">2. subprocess</h3>
<p  data-ke-size="size16">os.popen(), os.read()로 읽기 형태의 객체로 반환하여 문자열로 출력하거나, 문자열을 저장, parsing 하는 방법보다 더 쉬운 방법이 있다.</p>
<h4 id="1-subprocesscheck_out"  data-ke-size="size20">(1) subprocess.check_out</h4>
<blockquote  data-ke-style="style1">
<p data-ke-size="size16">check_out(명령어, shell에서 실행될것 인지의 여부, 바이너리 형태의 결과를 txt파일로 저장하기 위한 encoding format)</p>
</blockquote>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="routeros"><code>output = subprocess.check_out("cmd", shell=True, encoding='utf-8')
</code></pre>
</div>
</div>
<h3 id="2-subprocesscall"  data-ke-size="size23">(2) subprocess.call</h3>
<p  data-ke-size="size16">os.system과 같이 단순히 &ldquo;실행&rdquo;만 시킬 때는 &ldquo;call&rdquo; 메서드를 이용하면</p>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="gradle"><code>import subprocess

subprocess.call('ls -al', shell=True)
</code></pre>
</div>
</div>
<h3 id="3-subprocesspopen-은-call과-함께-사용하게-된다"  data-ke-size="size23">(3) subprocess.Popen() 은 call()과 함께 사용하게 된다.</h3>
<p  data-ke-size="size16">Popen으로 실행한 프로그램을 실행을 기다렸다가, 실행이 완료되었을 때 결과를 받을 수 있는 것이 call인것이다.</p>
<h4 id="참고"  data-ke-size="size20"><b>참고</b></h4>
<p  data-ke-size="size16">*args vs **kwargs 차이 *args : 파라미터를 2개 이상 넘기는 경우 *args **kwargs : *args처럼 파라미터를 2개 이상 넘기는데, **kwargs는 key를 설정할 수 있다. dictionary 형태의 값을 전달한다. (키워드 = 특정 값 형태로 함수를 호출할 수 있다.)</p>
<h3 id="with--as-"  data-ke-size="size23"><b>with ~ as ~</b></h3>
<p  data-ke-size="size16">프로세스를 종료하는 로직이 필요한 경우에 close( )가 없더라도 with ~ as ~ 구문이 끝나면 자동으로 객체를 close 하게 해준다</p>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="sql"><code>def call(*popenargs, timeout=None, **kwargs):

    with popen(*popenargs, **kwargs) as P:
        try:
            return p.wait(timeout=timeout)
        except:
            p.kill()
            raise
</code></pre>
</div>
</div>
<h3 id="wait-비동기를-사용하여-실행-결과를-대기하여-받을-수-있다"  data-ke-size="size23">wait 비동기를 사용하여 실행 결과를 대기하여 받을 수 있다.</h3>
<p  data-ke-size="size16"><b>treading 모듈의 wait()</b></p>
<blockquote  data-ke-style="style1">
<p data-ke-size="size16">import threading</p>
</blockquote>
<p  data-ke-size="size16">wait() 는 non-blocking, time.sleep()는 blocking 이다. time.sleep()은 호출이 끝날 때까지 스레드가 계속 실행되는 것을 차단하는 차이이다. sleep()시간적으로 기다릴 뿐이다. wait()는 실행 결과를 기다린다.</p>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="ini"><code>returncode = call(*args, **kwargs)

returncode = Popen(*args, **kwargs).wait()
</code></pre>
</div>
</div>
<h3 id="communicate--해당-명령이-종료될-때까지-대기"  data-ke-size="size23">communicate() : 해당 명령이 종료될 때까지 대기<span></span></h3>
<div style="background-color: #263238; color: #eeffff; text-align: start;">
<div>
<pre class="nimrod"><code>proc = subprocess.Popen(...)
try:
    out, errs = proc.communicate(timeout=10)
except subprocess.TimeoutExpired:
    proc.kill()
</code></pre>
</div>
</div>
<p  data-ke-size="size16">subprocess.Popen으로 생성된 객체에 communicate 함수를 사용하면 해당 명령이 종료될 때까지 대기한다. (timout 속성에 시간을 지정할수 있다.)</p>
<div style="background-color: #252a34; color: #eaeaea; text-align: center;">
<div id="aswift_2_host">&nbsp;</div>
</div>
<p  data-ke-size="size16">communicate 함수에 의해 반환된 out은 표준 출력객체로 out.stdout으로 그 값을 구할수 있다.</p>
<blockquote  data-ke-style="style1">
<p data-ke-size="size16">subprocess 모듈은 새로운 프로세스를 생성하고, 그들의 입력/출력/에러 파이프에 연결하고, 반환 코드를 얻을 수 있도록 합니다. 이 모듈은 몇 가지 이전 모듈과 함수를 대체하려고 합니다:</p>
<h3 id="출처--httpsdocspythonorgko3librarysubprocesshtml" data-ke-size="size23">출처 : <a href="https://docs.python.org/ko/3/library/subprocess.html">https://docs.python.org/ko/3/library/subprocess.html</a><a style="color: #8cd2d5;" href="https://amirer21.github.io/python/python-ossystem-vs-subprocess/#%EC%B6%9C%EC%B2%98--httpsdocspythonorgko3librarysubprocesshtml"><span>Permalink</span></a></h3>
</blockquote>