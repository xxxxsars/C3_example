1.安裝Flask與Pyodbc三個套件，Flask套件為Python 的web framwork，用來執行C3.js套件，pyodbc則是用來將SQl server資料與python做串接    
```python
pip install Flask,pyodbc
```    
若使用python3.5版安裝pyodbc會出現不支援的問題，請至[此網址下載](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyodbc)pyodbc.whl檔並安裝，whl安裝語法如下
```
cd "檔案所在跟目錄"
pip install pyodbc-3.0.10-cp35-none-win32.whl
```

2.下載C3.js與D3.js(雖然使用C3但C3的基礎建立在D3之上故還是需要引用D3檔案)    
[C3.JS](https://github.com/c3js/c3/archive/0.4.11.zip)    
[D3.JS](https://github.com/d3/d3/releases/download/v4.2.6/d3.zip)

3.引用JS file 到html檔案中，引用方式有底下兩種方式，並提供相關語法
+  利用網址引用(只需要在html檔案中的head標籤引用以下語法即可)
```JavaScript
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/d3/3.4.11/d3.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/c3/0.1.29/c3.js"></script>
<link href="//cdnjs.cloudflare.com/ajax/libs/c3/0.1.29/c3.css" rel="stylesheet" type="text/css">
```
+  利用自行下載的JS檔案引用   
(這邊的src擇要對應你所存放的c3與d3的js，以及c3的css，這邊要注意的是flask讀取相關的css與js需要放在static資料夾下，因此建議參閱下圖的存放方式，將c3與d3相關檔案分別放入兩個資料夾中，再將兩資料夾放入static資料夾下以便flask讀取)
![](https://raw.githubusercontent.com/xxxxsars/C3_example/master/pic/c3_path.png)
```JavaScript
<link href="../static/c3/c3.min.css" rel="stylesheet" type="text/css">
<script src="../static/c3/c3.min.js" ></script>
<script src="../static/d3/d3.js" charset="utf-8"></script>
```
