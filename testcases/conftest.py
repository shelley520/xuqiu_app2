import shlex
import signal
import subprocess
import os
import pytest
import time


@pytest.fixture(scope="class",autouse=True)
def record_vedio():
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # cmd = shlex.split("scrcpy --record %sfile.mp4"%now)
    # p = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    # yield
    # p.kill()
    # os.kill(p.pid,signal.CTRL_C_EVENT)
    # p.kill()
     #视频教程办法，但是不起作用

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    cmd = shlex.split("scrcpy --record %sfile.mp4" % now)
    with open("%sfile.mp4"%now,"w",encoding="utf-8") as f:
        p = subprocess.Popen(cmd, shell=False, stdout=f, stderr=subprocess.STDOUT)
    yield
    p.kill()



