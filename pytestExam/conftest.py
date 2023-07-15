from datetime import datetime
from py.xml import html
import pytest
import sys
import logging

# 출처 : https://pytest-html.readthedocs.io/en/latest/user_guide.html

#html 파일 생성
# pytest --html=report.html --self-contained-html
# pytest --html=report/report.html sample_pytest.py

'''보고서 제목'''
def pytest_html_report_title(report):    
    report.title = "My PyTest Title"
    pass

'''요약 섹션을 편집'''
#@pytest.mark.optionalhook
pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):    
    # prefix.extend([html.h3("Adding prefix message")])
    # summary.extend([html.h3("Adding summary message")])
    # postfix.extend([html.h3("Adding postfix message")])
    pass    

'''테스트를 실행하기 전에 환경 섹션을 수정'''
def pytest_configure(config):    
    # print(sys._getframe(0).f_code.co_name)
    # # getting user name
    # from pwd import getpwuid
    # from os import getuid

    # username = getpwuid(getuid())[0]

    # # getting python version
    # from platform import python_version
    # py_version = python_version()
    # # overwriting old parameters with  new parameters
    # config._metadata =  {
    #     "user_name": username,
    #     "python_version": py_version,
    #     "date": "오늘"
    # }
    pass
    

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        # extra.append(pytest_html.extras.url('./assets/image.png'))
        #extra.append(pytest_html.extras.text(item.name))

        # extra.append(pytest_html.extras.text('some string', name='Different title'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra