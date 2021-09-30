如果兼容http://127.0.0.1:8000/hello/ ，需要修改route:@app.route('/hello/') 这样 http://127.0.0.1:8000/hello/和http://127.0.0.1:8000/hello都可以访问。访问http://127.0.0.1:8000/hello会

重定向到http://127.0.0.1:8000/hello/

app.run(host='0.0.0.0',debug=True,port='8000')

debug=True 时，修改内容，会自动重启服务器，方便调试。