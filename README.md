# 58DataSpider-Python

## Installation

This project requires `pyquery`
If you have pip installed on your pc, you can install it by running  
`pip install pyquery`

### for mac user

1. install `libxml2`&&`libxslt` and link them with homebrew first
```
brew install libxml2
brew install libxslt
brew link libxml2 --force
brew link libxslt --force
```
2. then you can install pip according to [the document here](https://pip.pypa.io/en/stable/installing/)

3. at last run `pip install pyquery`, you will be ready to go.

## Usage

只需更改`Spider.py`文件即可
获取搜索分类，在58搜索你需要的关键词，然后截取58.com/xxx/中的xxx(分类信息)替换到文件最下方的Spider得构造函数中  
如 
```
spider = Spider('老肖的58助手', 'wh', 'kongtiao', '空调维修')
spider = Spider('老肖的58助手', 'sh', 'shejipeixun', '设计培训')
spider.getData()
```
