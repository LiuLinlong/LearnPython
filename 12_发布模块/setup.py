"""
发布模块
制作发布压缩包的步骤
    创建 setup.py

"""


from  distutils.core import setup

# 参数类型——多值字典参数
setup(name="lll_message",
      version="1.0",
      description="LLL的发送和接收消息模块",
      long_description="完整的发送和接收消息模块",
      author="Liu Linlong",
      author_email="liulinlong0325@outlook.com",
      url="none",
      py_modules = ["lll_message.send_message",
                    "lll_message.receive_message"])

"""
构建模块
这个文件需要用终端执行
python3 setup.py build

生成发布压缩包（在终端下）
python3 setup.py sdist

"""

"""
安装模块

终端中
tar -zxvf lll_message-1.0.tar.gz
sudo python3 setup.py install


卸载模块
cd ~/user/local/lib/python3.x/dist-packages/  # 这个路径可以import后 .__file__
sudo rm -r lll_message*
"""