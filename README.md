# snippet
python snippet daemon in the work


## 关于github上的代理设置

### 使用http协议

> git clone https://github.com/owner/git.git


```
# HTTP 代理
git config --global http.proxy "http://127.0.0.1:8080"
git config --global https.proxy "http://127.0.0.1:8080"

# socks5 代理（如 Shadowsocks）
git config --global http.proxy "socks5://127.0.0.1:1080"
git config --global https.proxy "socks5://127.0.0.1:1080"

# 取消设置
git config --global --unset http.proxy
git config --global --unset https.proxy`
```


### 使用ssh的方式

- 修改 ~/.ssh/config 文件（不存在则新建）：

```
# 必须是 github.com
Host github.com
   HostName github.com
   User git
   # HTTP 代理（如果这个方式，打开注释)
   # ProxyCommand socat - PROXY:127.0.0.1:%h:%p,proxyport=8080
   # socks5 代理（如 Shadowsocks）
   ProxyCommand nc -v -x 127.0.0.1:1080 %h %p

   ## windows
   # ProxyCommand connect -S 127.0.0.1:1080 %h %p


```
