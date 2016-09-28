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

3.建立index.html頁面
+  第一步建立基本html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
```   
+   建立JavaScript的語法區塊，在body tag中加入以下語法，這邊的function   myConcat為讀取Flask送來的資料透過處理後轉換成C3能讀取的array
    會傳回一個重資料庫讀取的array檔，其中此function有兩個參數，因為C3需要給予資料命名，因此地一個參數為命名，第二個參數才是要處理重python來的list
    ，轉換為c3所要的array，someJavaScriptvar與someJavaScriptvar2為讀取Flask來的資料，並在丟給myConcatfunction處理
```
<div id="chart"></div>
<script>

function myConcat(col_name,arguments) {
   var array_data = [col_name.toString()]
   for (var i = 0; i < arguments.length; i++) {
      array_data.push(arguments[i]);
   }
   return array_data;
}

var someJavaScriptVar = {{ data1 }};
var someJavaScriptVar2 = {{ data2 }};

var data1 =myConcat("data1",someJavaScriptVar)
var data2 = myConcat("data2",someJavaScriptVar2)

var chart = c3.generate({
    data: {
        columns: [

            data1,
            data2
        ]
    },
    axis: {
        x: {
            type: 'category',
            categories: ['cat1', 'cat2', 'cat3','cat4','cat5','cat6','cat7']
        }
    }
});
</script>
```

4.引用JS file 到html檔案中，引用方式有底下兩種方式，並提供相關語法
+  利用網址引用(只需要在html檔案中的head標籤引用以下語法即可)
```JavaScript
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/d3/3.4.11/d3.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/c3/0.1.29/c3.js"></script>
<link href="//cdnjs.cloudflare.com/ajax/libs/c3/0.1.29/c3.css" rel="stylesheet" type="text/css">
```
+  利用自行下載的JS檔案引用   
(這邊的src擇要對應你所存放的c3與d3的js，以及c3的css，這邊要注意的是flask讀取相關的css與js需要放在static資料夾下，因此建議參閱下圖的存放方式，將c3與d3相關檔案分別放入兩個資料夾中，再將兩資料夾放入static資料夾下以便flask讀取)   
![C3路徑圖](https://raw.githubusercontent.com/xxxxsars/C3_example/master/pic/c3_path.png)
![D3路徑圖](https://github.com/xxxxsars/C3_example/blob/master/pic/D3_path.png?raw=true)
```JavaScript
<link href="../static/c3/c3.min.css" rel="stylesheet" type="text/css">
<script src="../static/c3/c3.min.js" ></script>
<script src="../static/d3/d3.js" charset="utf-8"></script>
```

5.資料庫準備   
```SQL
CREATE TABLE [dbo].[C3](
	[Data1] [int] NULL,
	[Data2] [int] NOT NULL
) ON [PRIMARY]
```
