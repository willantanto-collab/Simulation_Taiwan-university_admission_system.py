import hashlib #Standard python library for cyptographic hashing
#Hash function like SHA-256 are one-way function: easy to compute,hard to reverse.
#Used here to create unique fingerprints of document for integrity vertification.
#Hash : a fixed-length unique fingerprint representing some data
class SecureDocument:
    def __init__(self,name,content = Name,student = None):
        self.name = name
        self.content = content or "" #Write or "" ensures the node always has a string,preventing error in hash computation if content is missing.
        self.student = student or [] #Similar logic as the self.content = content or ""
        self.hash = self.generate_hash() #Computes a fingerprint of this node and its subtree for furture integrity checks
    def generate_hash(self): #calculates a SHA-256 fingerprint using this node's conetnt plus all students
        combined = self.content
        for stud in self.student:
            combined += stud.hash
        return hash.lib.sha256(combined.encode()).hexdigest()) #converts content to bytes and creates a unique fingerprint for integrity vertification
        #return hash.lib.sha256(combined.encode()).hexdigest()) turn the string from human language into machine code
#Knowledge about this class Securedocument known by self-study.
class SecurityVertifier:
    def vertify(self,document):
        return self.vertify_recursive(document) #starts recursive check from root node
    def vertify_recursive(self,node):
        recalculated = node.content
        for stud in node.student: #veritify all child node
            if not self.vertify_recursive(stud): #if any student fail vertify,stop immediately
                return False
            recalculated += stud.hash #after child vertification,include its hash in parent's recompute
        recalculated  = hashlib.sha256(recalculated.encode()).hexdigest() #recalculate hash for this node
        if recalculated_hash != node.hash:
            print(f"Change of data detected in {node.name}")
            return False #any child tamper triggers in root invalidation
        return True
class SearchManager:
    def __init__(self, data_list):
        self.__data = data_list  
        self.comparisons = 0     
        self._cache = {}  # 缓存，避免重复的行为计算
    def linear_search(self, target):
        if target in self._cache:  # 增加缓存检查，如果找过就直接给结果
            return self._cache[target]
        for index, value in enumerate(self.__data): # 使用 enumerate 替代 range(len())，更简洁高效，他是用来循环时自动一边点名，一边报数，不用自己动手写代码去数现在是第几个的一种流程。
            self.comparisons += 1
            if value == target:
                self._cache[target] = index #存入缓存
                return index  
        self._cache[target] = -1
        return -1
#Scapy,初次尝试防守黑客攻击者的代码
#自学来的，自学链接用的这个 https://www.youtube.com/watch?v=f4Pr2X98UfE 和其他搜索来源
#https://www.youtube.com/watch?v=f4Pr2X98UfE 这个链接主要讲的是黑客用scapy 的基础攻击手段。
#所以我尝试去理解攻击者的攻击，并试着用代码来反过来从他们攻击的方式防守。我先去理解他们的攻击逻辑。
#还有就是，我写中文注释时担心兼容性，所以专门去查了 Python 编码规范，添加了下面这一行，这个coding and utf8
# -*- coding: utf-8 -*-
from scapy.all import sniff,IP,TCP

def trace_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP): #只关注具有潜在攻击特征的TCP 数据包
      src_ip = packet[IP].src #[IP]：打开packet的外壳，查看网络层（IP层）。.src：Source 是发件人的 IP 地址。.dst：Destination（目的地）是收件人的 IP 地址。
      dst_ip = packet[IP].dst
      if packet[TCP].flags == "S": #模拟黑客追踪，如果发现某个IP 在短时间尝试了大量的SYN 同步包.flags：查看这个包的标志说法，S 代表 SYN，SYN 同步的意思
        print(f"追踪痕迹，查找潜在扫描行为：{src_ip} -> {dst_ip}")#实时反馈：显示攻击源 IP 到目标 IP 的流向
        save_evidence_to_github_style_log(src_ip,"端口扫描尝试")#调用日志函数：将攻击源和行为特征存入本地文件，进行安全取证

def save_evidence_to_github_style_log(ip,behaviour): #Log 是程序在运行过程中，自动记录下来的事件信息。
  with open("forensics_report.log","a", encoding="utf-8") as f: # 使用 with 确保文件操作安全关闭，"a" 模式是为了把新发现的攻击证据追加到日志末尾而不覆盖旧记录。
    f.write(f"IP: {ip} ,行为：{behaviour},状态：已取证\n") # \n 是换行符，确保每条攻击证据独立成行，方便后续自动化审计和搜索。

print("正在尝试监控网络痕迹...需要管理员权限")
sniff(filter = "ip",prn = trace_packet,count = 10) #count = 10 意思是抓取10 个包演示，prn 是回调函数

#!/usr/bin/env python3
# 以上一行，我在 GitHub 上看一些开源的网络安全项目（比如 Scapy 的官方文档或相关的网络工具）时，发现其他代码写的厉害的文件开头都有这行。
# 我查了一下，发现这是为了在 Linux 环境下能直接运行，所以我专门在平板上手打加了进去。
def forensic_check_layer4(packet)： # 从wireshark scapy 学的，将逻辑重构为“数字鉴识”(Forensics) 检查
    #针对Layer 4 判定“意图”与“响应”
    #S = 侵入企图 (SYN)；SA = 目标响应 (SYN-ACK)
  if packet.haslayer(scapy.TCP): # 过滤 Layer 4 传输层：确保后续操作聚焦于 TCP 协议逻辑
    flags = packet[scapy.TCP].flags # 提取封包控制标志位：获取 SYN/ACK 等意图判定的核心元数据（metadata)
    # 核心判定：如果只有 SYN，代表扫描或企图侵入
    if flags == "S":
      return "检测到SYN扫描:法律判定为“侵入企图”"
    elif flags == "SA":
      return "检测到SYN-ACK:目标响应，连接正在建立"
    elif flags == "A": # ACK：标志三次握手完成，连接进入“实质侵害”阶段
      return "检测到 ACK:连接已建立，法律判定为”实质侵入”"
    return "非 TCP 关键封包" #默认返回：过滤非握手阶段的背景流量，确保鉴识逻辑的精准度

def send_covert_packet(target, message):
    print(f"正在通过 Layer 3 协议向 {target} 发送隐蔽数据...")
    # 构造 IP 层 (Layer 3)
    # 初始化 IPv4 报头 (符合 RFC 791 标准)
    # 在 6G/IoT 仿真中，该字段用于标识边缘计算节点或受控终端
    ip_layer = IP(dst=target)  # dst (Destination Address): 目标 IP 字段，决定了 Layer 3 路由的终点

    #协议封装逻辑 (Protocol Stack Construction)
    # 利用 Scapy 的层叠操作符 (/) 构造非标准协议栈
    # Layer 3 (IP）： 处理寻址与路由
    # Layer 3.5 (ICMP)： 绕过 Layer 4 (TCP) 的三次握手损耗
    # Payload (Raw Data)： 将 6G 存证指令 (RPG-791) 注入 ICMP 载荷区，实现极简信令传输
    icmp_packet = ip_layer / ICMP() / message 

    # 执行 Layer 3 原始套接字注入 (Raw Socket Injection)
    # 绕过系统标准传输层规制，直接将封装好的 ICMP 帧投递至链路层
    # verbose=False: 减少 I/O 开销，适用于 6G 边缘节点的高频信令仿真
    # 发送数据包
    #"Sent 1 packets"，查阅Scapy官方help(send)确认verbose参数控制输出
    # 运行这个使用的工具：Python IDE
    # 发现过程：while循环模拟6G心跳时，控制台被"Sent 1 packets"刷屏，导致无法观察L3载荷。
    # 解决逻辑：在终端输入 help(send) 查阅函数定义，发现 verbose 参数默认为开启，平板设为 False 以保持控制台整洁
    send(icmp_packet, verbose=False)
    print(f"数据包已发出，载荷长度: {len(message)} bytes") # 通过Wireshark观察到Data字段动态变化，故用Python内置len()实时监控L3载荷大小以评估通信效率
if __name__ == "__main__":
    # 模拟 RPG 791 项目中的自动化质询指令发送
    print("模拟环境(RPG-791)")
    try:
        while True:
            send_covert_packet(TARGET_IP, SECRET_DATA)
            # 设置 5 秒实验间隔。源于平板运行环境的性能限制，且为了手动对齐 Wireshark 抓包序列与代码输出，确保能逐帧分析 L3 字段
            time.sleep(5)  #实现非连续性信令传输 (Asynchronous Signaling)，模拟 6G/IoT 低功耗模式下的“心跳频率”
    except KeyboardInterrupt: # 针对平板(Pydroid 3等)运行环境，捕获点击停止按钮产生的信号，避免控制台弹出一整屏红色的报错代码
        print("\n 实验停止")
