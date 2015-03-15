<!DOCTYPE HTML>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta name="Keywords" content="blog"/>
    <meta name="Description" content="blog"/>
    <title>Simple</title>
    <link rel="shortcut icon" href="/static/favicon.png"/>
    <link rel="stylesheet" type="text/css" href="/main.css" />
</head>
<body>
<div class="main">
    <div class="header">
    	<ul id="pages">
            <li><a href="/">home</a></li>
            <li><a href="/#/tags">tags</a></li>
            <li><a href="/#/archive">archive</a></li>
    	</ul>
    </div>
	<div class="wrap-header">
	<h1>
    <a href="/" id="title"></a>
	</h1>
	</div>
<div id="md" style="display: none;">
<!-- markdown -->
之前根据flask文档做过一个简易博客[flaskblog](https://github.com/huangnauh/flaskblog)

这是看《flask web开发》这本书时的一些笔记

## 1 上下文
Falsk使用上下文让特定的变量临时在一个线程中全局可访问，与此同时却不会干扰其他线程。

在 Flask 中有两种上下文：程序上下文和请求上下文。

1. `current_app`是程序上下文，当前激活程序的程序实例
2. `g`是程序上下文，处理请求时用作临时存储的对象。每次请求都会重设这个变量
3. `request`是请求上下文，封装了客户端发出的 HTTP请求中的内容
4. `session`是请求上下文，用于存储请求之间的词典

## 2 请求钩子
在处理请求之前或之后执行代码

1. `before_first_request`：注册函数，在处理第一个请求之前运行。
2. `before_request` ：注册函数，在每次请求之前运行。
3. `after_request`：注册函数，如果没有未处理的异常抛出，在每次请求之后运行
4. `teardown_request`：注册函数，即使有未处理的异常抛出，也在每次请求之后运行

在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g

## 3 响应
(字符串作为HTML页面回送客户端,状态码,字典可以添加到HTTP响应中）

如果不想返回由1个、2个或3个值组成的元组，视图函数还可以返回Response对象。make_response()函数可接受1个2个或3个参数（和视图函数的返回值一样），并返回一个Response对象.
例如
```
@app.route('/') 
def index(): 
    response = make_response('<h1>This document carries a cookie!</h1>') 
    response.set_cookie('answer', '42') 
    return response
```

## 4 模板
为了业务逻辑和表现逻辑分离

Jinja2 能识别所有类型的变量，例如列表、字典和对象
```
<p>A value from a dictionary: {{ mydict['key'] }}.</p> 
<p>A value from a list: {{ mylist[3] }}.</p> 
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p> 
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

过滤器修改变量
```
首字母大写形式显示变量name的值
Hello, {{ name|capitalize }}
```

## 5 大型程序的结构

### 5.1 使用工厂函数
单个文件开发时，app在全局作用域中创建，无法动态修改配置
把创建过程移到可显式调用的工厂函数中,可以给脚本留出配置程序的时间，还能够创建多个程序实例.

### 5.2 使用蓝本
转换成程序工厂函数后,程序在运行时创建，只有调用 `create_app()` 之后才能使用 `app.route` 修饰器,同样错误页面处理程序使用 `app.errorhandler` 修饰器定义

蓝本和程序类似，也可以定义路由。不同的是，在蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正成为程序的一部分。

注册蓝本:
````
def create_app(config_name): 
    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint) 
    return app
```

蓝本中的错误处理程序
```
from flask import render_template 
from . import main 
@main.app_errorhandler(404) 
def page_not_found(e): 
    return render_template('404.html'), 404 
```


`url_for()`函数的第一个参数是路由的端点名，在程序的路由中，默认为视图函数的名字.
而蓝本中的全部端点都加上了一个命名空间，可以在不同的蓝本中使用相同的端点名定义视图函数，而不会产生冲突。命名空间就是蓝本的名字。

```
url_for('.index')
url_for('main.index')
```

<!-- markdown end -->
</div>
<div class="entry" id="main">
<!-- content -->
<p>之前根据flask文档做过一个简易博客<a href="https://github.com/huangnauh/flaskblog">flaskblog</a></p>

<p>这是看《flask web开发》这本书时的一些笔记</p>

<h2 id="1">1 上下文</h2>

<p>Falsk使用上下文让特定的变量临时在一个线程中全局可访问，与此同时却不会干扰其他线程。</p>

<p>在 Flask 中有两种上下文：程序上下文和请求上下文。</p>

<ol>
<li><code>current_app</code>是程序上下文，当前激活程序的程序实例</li>
<li><code>g</code>是程序上下文，处理请求时用作临时存储的对象。每次请求都会重设这个变量</li>
<li><code>request</code>是请求上下文，封装了客户端发出的 HTTP请求中的内容</li>
<li><code>session</code>是请求上下文，用于存储请求之间的词典</li>
</ol>

<h2 id="2">2 请求钩子</h2>

<p>在处理请求之前或之后执行代码</p>

<ol>
<li><code>before_first_request</code>：注册函数，在处理第一个请求之前运行。</li>
<li><code>before_request</code> ：注册函数，在每次请求之前运行。</li>
<li><code>after_request</code>：注册函数，如果没有未处理的异常抛出，在每次请求之后运行</li>
<li><code>teardown_request</code>：注册函数，即使有未处理的异常抛出，也在每次请求之后运行</li>
</ol>

<p>在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g</p>

<h2 id="3">3 响应</h2>

<p>(字符串作为HTML页面回送客户端,状态码,字典可以添加到HTTP响应中）</p>

<p>如果不想返回由1个、2个或3个值组成的元组，视图函数还可以返回Response对象。make_response()函数可接受1个2个或3个参数（和视图函数的返回值一样），并返回一个Response对象.
例如</p>

<pre><code>@app.route('/') 
def index(): 
    response = make_response('&lt;h1&gt;This document carries a cookie!&lt;/h1&gt;') 
    response.set_cookie('answer', '42') 
    return response
</code></pre>

<h2 id="4">4 模板</h2>

<p>为了业务逻辑和表现逻辑分离</p>

<p>Jinja2 能识别所有类型的变量，例如列表、字典和对象</p>

<pre><code>&lt;p&gt;A value from a dictionary: {{ mydict['key'] }}.&lt;/p&gt; 
&lt;p&gt;A value from a list: {{ mylist[3] }}.&lt;/p&gt; 
&lt;p&gt;A value from a list, with a variable index: {{ mylist[myintvar] }}.&lt;/p&gt; 
&lt;p&gt;A value from an object's method: {{ myobj.somemethod() }}.&lt;/p&gt;
</code></pre>

<p>过滤器修改变量</p>

<pre><code>首字母大写形式显示变量name的值
Hello, {{ name|capitalize }}
</code></pre>

<h2 id="5">5 大型程序的结构</h2>

<h3 id="51">5.1 使用工厂函数</h3>

<p>单个文件开发时，app在全局作用域中创建，无法动态修改配置
把创建过程移到可显式调用的工厂函数中,可以给脚本留出配置程序的时间，还能够创建多个程序实例.</p>

<h3 id="52">5.2 使用蓝本</h3>

<p>转换成程序工厂函数后,程序在运行时创建，只有调用 <code>create_app()</code> 之后才能使用 <code>app.route</code> 修饰器,同样错误页面处理程序使用 <code>app.errorhandler</code> 修饰器定义</p>

<p>蓝本和程序类似，也可以定义路由。不同的是，在蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正成为程序的一部分。</p>

<p>注册蓝本:</p>

<pre><code class="`">def create_app(config_name): 
    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint) 
    return app
</code></pre>

<p>蓝本中的错误处理程序</p>

<pre><code>from flask import render_template 
from . import main 
@main.app_errorhandler(404) 
def page_not_found(e): 
    return render_template('404.html'), 404 
</code></pre>

<p><code>url_for()</code>函数的第一个参数是路由的端点名，在程序的路由中，默认为视图函数的名字.
而蓝本中的全部端点都加上了一个命名空间，可以在不同的蓝本中使用相同的端点名定义视图函数，而不会产生冲突。命名空间就是蓝本的名字。</p>

<pre><code>url_for('.index')
url_for('main.index')
</code></pre>
<!-- content end -->
</div>
<br>
<br>
    <div id="disqus_thread"></div>
	<div class="footer">
		<p>© Copyright 2014 by isnowfy, Designed by isnowfy</p>
	</div>
</div>
<script src="main.js"></script>
<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ["\\(", "\\)"]], processEscapes: true}});
</script>
<script id="content" type="text/mustache">
    <h1>{{title}}</h1>
    <div class="tag">
    {{date}}
    {{#tags}}
    <a href="/#/tag/{{name}}">#{{name}}</a>
    {{/tags}}
    </div>
</script>
<script id="pagesTemplate" type="text/mustache">
    {{#pages}}
    <li>
        <a href="{{path}}">{{title}}</a>
    </li>
    {{/pages}}
</script>
<script>
$(document).ready(function() {
    $.ajax({
        url: "main.json",
        type: "GET",
        dataType: "json",
        success: function(data) {
            $("#title").html(data.name);
            var pagesTemplate = Hogan.compile($("#pagesTemplate").html());
            var pagesHtml = pagesTemplate.render({"pages": data.pages});
            $("#pages").append(pagesHtml);
            //path
            var path = "flask-learning.py";
            //path end
            var now = 0;
            for (var i = 0; i < data.posts.length; ++i)
                if (path == data.posts[i].path)
                    now = i;
            var post = data.posts[now];
            var tmp = post.tags.split(" ");
            var tags = [];
            for (var i = 0; i < tmp.length; ++i)
                if (tmp[i].length > 0)
                    tags.push({"name": tmp[i]});
            var contentTemplate = Hogan.compile($("#content").html());
            var contentHtml = contentTemplate.render({"title": post.title, "tags": tags, "date": post.date});
            $("#main").prepend(contentHtml);
            if (data.disqus_shortname.length > 0) {
                var disqus_shortname = data.disqus_shortname;
                (function() {
                    var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                    dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
                    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
                })();
            }
        }
    });
});
</script>
</body>
</html>
