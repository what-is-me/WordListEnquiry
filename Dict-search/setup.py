'''
Author: what-is-me
E-mail: nt_cqc@126.com
Github: https://github.com/what-is-me
LeetCode: https://leetcode-cn.com/u/what-is-me/
Date: 2021-05-18 00:33:31
LastEditors: what-is-me
LastEditTime: 2021-05-18 02:02:36
Description: file content
'''
import setuptools  # 导入setuptools打包工具
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="Dict_search",
    version="0.0.1",
    author="what-is-me",
    author_email="leo.cai.nantong.china@gmail.com",
    description="查询单个单词/词组意思",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/what-is-me/WordListEnquiry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)
