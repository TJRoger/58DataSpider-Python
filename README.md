# 58DataSpider-Python

## Installation

This project requires `pyquery`
If you have pip installed on your pc, you can install it by running  
`pip install pyquery`

### for mac user

* install `libxml2`&&`libxslt` and link them with homebrew first
```
brew install libxml2
brew install libxslt
brew link libxml2 --force
brew link libxslt --force
```
* then you can install pip according to [the document here](https://pip.pypa.io/en/stable/installing/)

* at last run `pip install pyquery`, you will be ready to go.

## Usage

只需更改`Spider.py`文件中得相应参数即可
* 获取搜索分类，在58搜索你需要的关键词，然后截取58.com/xxx/中的xxx(分类信息)替换到文件最下方的Spider得构造函数中第三个参数  
如 
```
spider = Spider('小小龙的58助手', 'wh', 'kongtiao', '空调维修')
spider = Spider('小小龙的58助手', 'sh', 'shejipeixun', '设计培训')
spider.getData()
```
在当前目录运行`python Spider.py`,运行完毕数据保存在58data/DATA.html中，数据填入方式为附加，所以每次运行过后请另行保存并删除或清空该文件
