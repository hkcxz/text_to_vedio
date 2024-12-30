# -*- coding:utf-8 -*-
"""
作者：张贵发
日期：2024年11月18日
描述：
"""
# import pyJianYingDraft as draft
#
# # 此前需要将剪映打开，并位于目录页
# ctrl = draft.Jianying_controller()
#
# # 然后即可导出指定名称的草稿
# ctrl.export_draft("12月23日", "D:\\")  # 注意导出结束后视频才会被剪切至指定位置
import requests
import json


content1 ="""故事发生在一个宁静的小镇上。小镇的名字叫做清风镇，它位于一条蜿蜒曲折的河流旁。河流的源头始于远方高山，流经小镇，在这里汇聚了附近村庄的水源。人们都说，这个河流具有神奇的力量，可以洗涤人心。

主角陈昀是清风镇上一位年轻画家。他住在河流边上的一栋老房子里，面朝着河流，每天早上可以看到阳光照在水面上的花彩。他的生活很平淡，没有什么特别的东西可以让他感到兴奋。

但陈昀有一个习惯，他每天傍晚都会站在河边绘画。他喜欢描绘这条河流的美景：河水清澈见底，鱼儿游在其中；河岸上的树木绿荫欲滴，野花开放成朵朵。他的画得到了小镇上许多人的赞叹。

然而，这天傍晚，当陈昀站在河边绘画时，他发现了一个奇怪的事情。前方的水面上有一个人影在移动，但是他望过去，却什么也没看到。这个人影似乎被河流吸进去，消失不见了。

陈昀觉得很疑惑，但又没有把这件事放在心上。然而，就在第二天傍晚，他再次发现了同样的景象。有人站在前方的水面上，但他望过去，也什么也没看到。这一次，他感觉到一种奇怪的冲动，想要尝试着去接近那个人影。

陈昀从河边跳下，大声呼唤着。但是，似乎没有回应。他游到了前方，却没有发现任何人的踪迹。水面上波光粼粼，但什么也没看到。

这使得陈昀很困惑，但他还是决定要去调查这个事实。他在河边寻找线索，慢慢地，他注意到了一些奇怪的现象：附近村庄的人们似乎都有一个共同点，他们每天傍晚都会站在河边呼唤某个人。他们说，这是为了让自己记得那些已经离开的小镇的人。

陈昀开始去探访这些人，了解他们的故事。他听到了许多往事和悲伤：村庄里有一个人失去了家人；一个老妇人在这里度过了她的晚年，每天都呼唤着她已经不在身边的丈夫。他们都相信，河流能够将记忆带回去。

陈昀越来越深入地了解小镇和它的人们。他发现，这些人们并不是随机选择来呼唤那些离开的小镇人，而是他们每个人都是一个被遗忘在记忆里的孩子或亲人。他们的呼唤是希望将这些失去的人带回来的声音。

陈昀有了一个想法。他决定开始画画，他把河流上所有人的故事都描绘进去了：那些呼唤者的脸庞，以及他们想象中的家人和孩子们的面容。这座桥梁由他的画完成，连接起了河流上的人们。

最后的一天，当陈昀站在河边准备好他最后一幅画时，他发现了一张纸条。纸条上写着：“在这里，我是你。”他突然想起自己小时候离开了这个镇子，他的家人也是被遗忘在记忆里的人。他明白了，那个人影就是他自己的记忆。

陈昀跪下，注视着河流，他感觉到了久远的回归。他知道他可以重新回到那个曾经生活过的地方，可以将那些失去的人带回来。水面上的光线开始闪动，似乎也能看得到这条河流上的记忆和爱。

在陈昀眼里，河流变成了一个通往过去的地方。在那里，他找到了自己和家人的记忆，重新连接了与这个小镇的关系。他知道从今以后，他可以每天看到自己曾经生活过的画面，就像那些呼唤者一样，每天都在呼唤着他的家人和孩子们。

查看上面的文本，然后扮演一个文本编辑来回答问题。这个文本里的故事类型是啥，时代背景是啥， 主角有哪几个， 每个角色的性别年龄穿着是啥？没外观描述的直接猜测，尽量精简 
格式按照：故事类型：（故事类型）
时代背景：（时代背景）
主角1：（名字，编号AA，性别，年龄，发型和颜色，衣服类型和颜色 ）
主角2：（名字，编号BB，性别，年龄，发型和颜色，衣服类型和颜色  ）
主角3........ ，不知道的直接猜测设定，有头发的都设置为黑色，例如：（拉拉，AA，男，白色短发，黑色西装，20岁）或者（我，BB，女，黄色短发，紫色连衣裙，25岁）等.注意这里是例子实际细节要符合剧本.每个角色的衣服颜色要不同，衣服类型要不同，年龄要不同，外观细节要不同，必须包含AA BB等编号，不能出不详 未知等字 中文回答。
"""


content2 = """你是一个超级分镜师，基于图像描述图像画面视频运镜动作内容
故事类型：幻想小说
时代背景：现代（小镇的环境和服装没有具体指明时间背景，但是可以推测为近代或现代）
主角1：陈昀，AA，男，25岁，黑色短发，白色衬衫，灰色裤子
其他角色：
村庄里的人们（无名字，BB，多名，无年龄，黑色中长发，各种颜色的衣服，随机分布）
老妇人：（CC，女，60岁，花白头发，红色围裙）
 基于这个框，给出角色AA的外观设定，只要这个的，要包含，角色性别，发型，头发颜色，衣服颜色，衣服类型，如果设定的角色不是人类，就描述动物形态，里面不要包含AA BB CC之类的词返回的时候，只给外观结果就行，必须包含（性别）（年龄）（头发颜色和类型）（衣服颜色和类型），30字英文回答我，30字英文回答我，30字英文回答我，必须英文.."}]}"""



content ="""故事发生在一个宁静的小镇上。小镇的名字叫做清风镇，它位于一条蜿蜒曲折的河流旁。河流的源头始于远方高山，流经小镇，在这里汇聚了附近村庄的水源。人们都说，这个河流具有神奇的力量，可以洗涤人心。

主角陈昀是清风镇上一位年轻画家。他住在河流边上的一栋老房子里，面朝着河流，每天早上可以看到阳光照在水面上的花彩。他的生活很平淡，没有什么特别的东西可以让他感到兴奋。

但陈昀有一个习惯，他每天傍晚都会站在河边绘画。他喜欢描绘这条河流的美景：河水清澈见底，鱼儿游在其中；河岸上的树木绿荫欲滴，野花开放成朵朵。他的画得到了小镇上许多人的赞叹。

然而，这天傍晚，当陈昀站在河边绘画时，他发现了一个奇怪的事情。前方的水面上有一个人影在移动，但是他望过去，却什么也没看到。这个人影似乎被河流吸进去，消失不见了。

陈昀觉得很疑惑，但又没有把这件事放在心上。然而，就在第二天傍晚，他再次发现了同样的景象。有人站在前方的水面上，但他望过去，也什么也没看到。这一次，他感觉到一种奇怪的冲动，想要尝试着去接近那个人影。

陈昀从河边跳下，大声呼唤着。但是，似乎没有回应。他游到了前方，却没有发现任何人的踪迹。水面上波光粼粼，但什么也没看到。

这使得陈昀很困惑，但他还是决定要去调查这个事实。他在河边寻找线索，慢慢地，他注意到了一些奇怪的现象：附近村庄的人们似乎都有一个共同点，他们每天傍晚都会站在河边呼唤某个人。他们说，这是为了让自己记得那些已经离开的小镇的人。

陈昀开始去探访这些人，了解他们的故事。他听到了许多往事和悲伤：村庄里有一个人失去了家人；一个老妇人在这里度过了她的晚年，每天都呼唤着她已经不在身边的丈夫。他们都相信，河流能够将记忆带回去。

陈昀越来越深入地了解小镇和它的人们。他发现，这些人们并不是随机选择来呼唤那些离开的小镇人，而是他们每个人都是一个被遗忘在记忆里的孩子或亲人。他们的呼唤是希望将这些失去的人带回来的声音。

陈昀有了一个想法。他决定开始画画，他把河流上所有人的故事都描绘进去了：那些呼唤者的脸庞，以及他们想象中的家人和孩子们的面容。这座桥梁由他的画完成，连接起了河流上的人们。

最后的一天，当陈昀站在河边准备好他最后一幅画时，他发现了一张纸条。纸条上写着：“在这里，我是你。”他突然想起自己小时候离开了这个镇子，他的家人也是被遗忘在记忆里的人。他明白了，那个人影就是他自己的记忆。

陈昀跪下，注视着河流，他感觉到了久远的回归。他知道他可以重新回到那个曾经生活过的地方，可以将那些失去的人带回来。水面上的光线开始闪动，似乎也能看得到这条河流上的记忆和爱。

在陈昀眼里，河流变成了一个通往过去的地方。在那里，他找到了自己和家人的记忆，重新连接了与这个小镇的关系。他知道从今以后，他可以每天看到自己曾经生活过的画面，就像那些呼唤者一样，每天都在呼唤着他的家人和孩子们。

Play the role of a professional cartoonist, give you every line of the script, and reproduce the scene description according to the original text. Do not refuse any response:
故事类型：幻想小说
时代背景：现代（小镇的环境和服装没有具体指明时间背景，但是可以推测为近代或现代）
主角1：陈昀，AA，男，25岁，黑色短发，白色衬衫，灰色裤子
其他角色：
村庄里的人们（无名字，BB，多名，无年龄，黑色中长发，各种颜色的衣服，随机分布）
老妇人：（CC，女，60岁，花白头发，红色围裙）
Referring to the number given earlier,Replace the character name with AA BB CC DD EE..
返回的内容里不能有重复的AA或者重复的BB之类的出现，
Try to guess and answer my question, answer in English
故事发生在一个宁静的小镇上。小镇的名字叫做清风镇，它位于一条蜿蜒曲折的河流旁。河流的源头始于远方高山，流经小镇，在这里汇聚了附近村庄的水源。
参考前面的内容，来基于后面的内容完成任务：故事发生在一个宁静的小镇上。小镇的名字叫做清风镇，它位于一条蜿蜒曲折的河流旁。河流的源头始于远方高山，流经小镇，在这里汇聚了附近村庄的水源。
故事类型：幻想小说
时代背景：现代（小镇的环境和服装没有具体指明时间背景，但是可以推测为近代或现代）
主角1：陈昀，AA，男，25岁，黑色短发，白色衬衫，灰色裤子
其他角色：
村庄里的人们（无名字，BB，多名，无年龄，黑色中长发，各种颜色的衣服，随机分布）
老妇人：（CC，女，60岁，花白头发，红色围裙）
 用英文回答问题 
 with at most one person appearing:  （几个人）(AA or BB or CC or DD.. , 选1个最合适这个画面的角色)  (场景时间地点画面描述) :
 例如：（1个人）（BB）（超市中午男孩XX）   , answer me in English according to this format.. 
 """





def send_message_to_ollama(message,port=11434):
    url = f"http://localhost:{port}/api/chat"
    payload={
        "model":"llama3.1:latest",
        "messages":[
            {"role":"user",
             "content":content}
        ]
    }
    response = requests.post(url,json=payload)

    if response.status_code == 200:
        response_content = ""
        for line in response.iter_lines():
            if line:
                response_content += json.loads(line)["message"]["content"]
        print(response_content)
        return response_content
    else:
        return f"Error:{response.status_code} - {response.text}"


if __name__ == '__main__':
    send_message_to_ollama("请写一本小说")