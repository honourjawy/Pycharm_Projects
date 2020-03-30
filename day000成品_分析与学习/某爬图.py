import urllib.request#http请求用到的模块
import re,os#正则表达式以及操作文件模块

url = "http://www.win4000.com/zt/erciyuan_1.html"#爬取的地址
# url = "http://www.win4000.com/zt/erciyuan_2.html"
# url = "http://www.win4000.com/zt/erciyuan_3.html"
# url = "http://www.win4000.com/zt/erciyuan_4.html"
# url = "http://www.win4000.com/zt/erciyuan_5.html"

web = urllib.request.urlopen(url).read()#加载url
web = web.decode('utf-8')#换成网页的编码可以了
#print(web)
res = r'<a\shref="(http://www.win4000.com/wallpaper_detail_[0-9]+.html)"\salt="'#使用原生字符串，阻止python解释器的转义
resn = r'<span>1</span>/<em>([0-9]+)</em>'#匹配图片的个数
resi = r'<img\sclass="pic-large"\ssrc="(http://pic1.win4000.com/wallpaper/[0-9]+-[0-9]+-[0-9]+/\w+.[g-p]+g)"\salt="'#匹配页面的图片URL
resp = r'(http://www.win4000.com/wallpaper_detail_[0-9]+).html'#提取出拼接字符串
resg = r'http://pic1.win4000.com/wallpaper/[0-9]+-[0-9]+-[0-9]+/\w+(.[g-p]+g)'#提取出图片的格式
lk = re.findall(res,web,re.S)#由于findall是逐行匹配，re.S使得匹配包含\n在内的所有字符
path = "D:\文件夹"#下载的图片保存的路径，一定得是这种格式，最后不能带斜杠
savep = os.path.exists(path)#判断该文件夹是否存在
if savep == False:
    print("该文件夹不存在，请重新修改路径")
    os._exit()#强退
nm = 0#图片的名字，依次递增
for line in lk:#依次循环http://www.win4000.com/zt/erciyuan_1.html的24个图集
    web = urllib.request.urlopen(line).read()
    web = web.decode('utf-8')#解析其中的一个页面
    num = re.findall(resn,web,re.S)#获取当前图集中图片的个数，遍历单个图集的时候方便跳转页面
    img = re.findall(resi,web,re.S)#获取当前页面内的图片链接
    fe = re.findall(resg,img[0],re.S)#获取图片的格式，便于保存的时候记录图片的名字
    urllib.request.urlretrieve(img[0],path+"/"+str(nm)+fe[0])#下载链接中指定的图片
    nm = nm + 1#名字顺序加一
    print("第" + str(nm) + "张下载完成")
    i = 2#该图集中的第二张图片页面
    while i <= int(num[0]):#while循环遍历图集
        strp = re.findall(resp,line,re.S)#提取出页面的拼接字符串的前半段
        webs = urllib.request.urlopen(strp[0]+"_"+str(i)+".html").read()
        webs = webs.decode('utf-8')#webs为当前图集的下一个页面
        imgs = re.findall(resi,webs,re.S)#当前页面的图片的URL
        fe = re.findall(resg, img[0], re.S)#提取图片的格式
        urllib.request.urlretrieve(imgs[0], path+"/"+str(nm)+fe[0])#拼接图片的保存地址，进行下载
        nm = nm + 1#图片名字顺序加一
        print("第" + str(nm) + "张下载完成")
        i = i + 1#该图集的图片页面顺序加一
print("下载完毕")
#吾爱破解：seattle^-^    手打