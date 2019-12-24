#Scapy Version:2.4.0
#Python Version:3.7.2
#作成日：2019/01/29 Ver 1.0
#作成者：笈川 萌

#更新日:2019/07/06 Ver 1.01
#更新者：中山
#更新内容: IPv6 LLMNR qtype="AAAA"を明示的に設定 : ICMPV6 Multicast Listener QueryのHopLimit=1設定  & 拡張ヘッダのHopByHopを追加 |Ver表示を追加

########
# 注意 #
########

# 1. テストプログラムを動かすPCのファイアウォールの設定を確認しておくこと（対象のパケットの送受信を行うには規則を「有効」にしておく必要がある）
# 2. "run_scapy"を実行してからテストプログラムを動かすこと
# 3. scapy-2.4.0\scapy\fields.py の NetBIOSNameField を修正してからテストプログラムを動かすこと
# 4. NotePCなどでWiFi/BlueToothなどがある場合は無効化すること(有線のみ使用したい場合)

#    <修正前>   x = b"".join(chb(0x41 + orb(b)>>4) + chb(0x41 + orb(b)&0xf) for b in x)
#
#                                        括弧を追加                 括弧を追加
#    <修正後>   x = b"".join(chb(0x41 + (orb(b)>>4)) + chb(0x41 + (orb(b)&0xf)) for b in x)


from scapy.all import *

###################################
# 実機に合わせて以下を変更して下さい #
###################################

DST_IP_V4 = "192.168.10.101"                    #送信先のIPv4アドレスを記入
DST_IP_V6 = "fe80::5a38:79ff:fe00:1982"         #送信先のIPv6アドレスを記入	#大元
#DST_IP_V6 = "ff80::5a38:79ff:fe00:1982" 										#無理やりマルチキャスト　消すこと

SRC_IP_V4 = "192.168.1.2"                    #送信元のIPv4アドレスを記入
SRC_IP_V6 = "fe80::d1de:b60:e26b:f9f5"          #送信元のIPv6アドレスを記入

NAME = "RNP583879001982"                        #送信先のNetBIOS名を記入（コマンドプロンプトより"nbtstat -A <IPアドレス>"）

uuid = 'bf6774d2-3e64-11e8-aca3-8662aadcadfa'   #送信先のUUIDを記入(シングルクォーテーションで記入すること)

#PCのIPv6設定にも手動設定アドレスを入れておくこと
DST_IP = [
          "2001:0db8:ffff:ffff:0226:73ff:fe0c:d60f", #送信先のIPv6手動設定アドレスを記入
          "fe80::5a38:79ff:fe00:1982",               #送信先のリンクローカルアドレスを記入
          "2001:aaaa::500",                          #送信先のDHCPv6アドレスを記入
          "2001:1000::dc39:fab1:30f4:4600",          #送信先のステートレスアドレス(1)を記入
          "2001:1000::dc39:fab1:30f4:4601",          #送信先のステートレスアドレス(2)を記入
          "2001:1000::dc39:fab1:30f4:4602",          #送信先のステートレスアドレス(3)を記入
          "2001:1000::dc39:fab1:30f4:4603",          #送信先のステートレスアドレス(4)を記入
          "2001:1000::dc39:fab1:30f4:4604",          #送信先のステートレスアドレス(5)を記入
          ]



class Tests:
    pass

    def run(self):
        print("PacketTestTool Ver 1.01")
        print("1.  IPv4 ARP Request")
        print("2.  IPv4 ICMP Echo Request")
        print("3.  IPv4 NetBIOS Name Service")
        print("4.  IPv4 SNMP")
        print("5.  IPv6 SNMP")
        print("6.  IPv4 LLMNR")
        print("7.  IPv6 LLMNR")
        print("8.  ICMPv6 Echo Request")
        print("9.  ICMPv6 Multicast Listener Query")
        print("10. IPv4 SSDP")
        print("11. IPv6 SSDP")
        print("12. IPv4 WS-Discovery")
        print("13. IPv6 WS-Discovery")
        print("14. IPv4 mDNS(Bonjour)")
        print("15. IPv6 mDNS(Bonjour)")
        print("16. IPv6 TCP")
        print("17. IPv6 UDP")
        print("18. ALL")
        print("---------------------------------------")
        print("19. Exit")
        print("")
        num = input("Choose The Test: ").rstrip()
        if num == "1":
            tests.arp()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "2":
            tests.icmp()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "3":
            tests.netbiosname()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "4":
            tests.snmp_ipv4()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "5":
            tests.snmp_ipv6()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "6":
            tests.llmnr_ipv4()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "7":
            tests.llmnr_ipv6()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "8":
            tests.icmpv6_echo()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "9":
            tests.icmpv6_multicast()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "10":
            tests.ssdp_ipv4()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "11":
            tests.ssdp_ipv6()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "12":
            tests.wsdiscovery_ipv4()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "13":
            tests.wsdiscovery_ipv6()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "14":
            tests.mdns_ipv4()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "15":
            tests.mdns_ipv6()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "16":
            tests.ipv6_TCP()
        elif num == "17":
            tests.ipv6_UDP()
        elif num == "18":
            tests.arp()
            tests.icmp()
            tests.netbiosname()
            tests.snmp_ipv4()
            tests.snmp_ipv6()
            tests.llmnr_ipv4()
            tests.llmnr_ipv6()
            tests.icmpv6_echo()
            tests.icmpv6_multicast()
            tests.ssdp_ipv4()
            tests.ssdp_ipv6()
            tests.wsdiscovery_ipv4()
            tests.wsdiscovery_ipv6()
            tests.mdns_ipv4()
            tests.mdns_ipv6()
            tests.ipv6_tcp_all()
            tests.ipv6_udp_all()
            num = input("\nPress Enter Key")
            tests.run()
        elif num == "19":
            exit()
        else:
            tests.run()

    def ipv6_TCP(self):
        print("")
        print("1. IPv6手動設定")
        print("2. リンクローカルアドレス")
        print("3. DHCPv6アドレス")
        print("4. ステートレスアドレス(1)")
        print("5. ステートレスアドレス(2)")
        print("6. ステートレスアドレス(3)")
        print("7. ステートレスアドレス(4)")
        print("8. ステートレスアドレス(5)")
        print("---------------------------------------")
        print("9. Back")
        print("")

        num = input("Choose The Test: ").rstrip()
        if num == "1":
            tests.ipv6_tcp_manual()
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "2":
            tests.ipv6_tcp_linklocal()
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "3":
            tests.ipv6_tcp_dhcp()
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "4":
            tests.ipv6_tcp_stateless(3)
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "5":
            tests.ipv6_tcp_stateless(4)
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "6":
            tests.ipv6_tcp_stateless(5)
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "7":
            tests.ipv6_tcp_stateless(6)
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "8":
            tests.ipv6_tcp_stateless(7)
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        elif num == "9":
            tests.run()
        else:
            tests.ipv6_TCP()

    def ipv6_UDP(self):
        print("")
        print("1. IPv6手動設定")
        print("2. リンクローカルアドレス")
        print("3. DHCPv6アドレス")
        print("4. ステートレスアドレス(1)")
        print("5. ステートレスアドレス(2)")
        print("6. ステートレスアドレス(3)")
        print("7. ステートレスアドレス(4)")
        print("8. ステートレスアドレス(5)")
        print("---------------------------------------")
        print("9. Back")
        print("")

        num = input("Choose The Test: ").rstrip()
        if num == "1":
            tests.ipv6_udp_manual()
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "2":
            tests.ipv6_udp_linklocal()
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "3":
            tests.ipv6_udp_dhcp()
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "4":
            tests.ipv6_udp_stateless(3)
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "5":
            tests.ipv6_udp_stateless(4)
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "6":
            tests.ipv6_udp_stateless(5)
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "7":
            tests.ipv6_udp_stateless(6)
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "8":
            tests.ipv6_udp_stateless(7)
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        elif num == "9":
            tests.run()
        else:
            tests.ipv6_UDP()

####################
# IPv4 ARP Request #
####################

    def arp(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=DST_IP_V4)
        srp1(pkt)

##########################
# IPv4 ICMP Echo Request #
##########################

    def icmp(self):
        pkt = Ether() / IP(dst=DST_IP_V4) / ICMP()
        srp1(pkt)

#############################
# IPv4 NetBIOS Name Service #
#############################

    #dstは"192.168.10.255"で固定
    #sport、dportは137で固定
    def netbiosname(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=NAME)
        sendp(pkt)

#############
# IPv4 SNMP #
#############

    #dportは161で固定
    def snmp_ipv4(self):
        p = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        sendp(p)

#############
# IPv6 SNMP #
#############

    #dportは161で固定
    def snmp_ipv6(self):
        p = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        sendp(p)

##############
# IPv4 LLMNR #
##############

    #dstは"224.0.0.252"で固定
    #dportは5355で固定
    def llmnr_ipv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=NAME))
        sendp(pkt)

##############
# IPv6 LLMNR #
##############

    #dstは"ff02::1:3"で固定
    #dportは5355で固定
    def llmnr_ipv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst="ff02::1:3")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=NAME,qtype=28))
        sendp(pkt)

#######################
# ICMPv6 Echo Request #
#######################

    def icmpv6_echo(self):
        pkt = IPv6(dst=DST_IP_V6) / ICMPv6EchoRequest()
        sr1(pkt)

###################################
# ICMPv6 Multicast Listener Query #
###################################

    def icmpv6_multicast(self):
        pkt = IPv6(dst=DST_IP_V6,hlim=1) /IPv6ExtHdrHopByHop() / ICMPv6MLQuery()
        send(pkt)

#############
# IPv4 SSDP #
#############

    #dstは"239.255.255.250"で固定
    #sport、dportは1900で固定\
    def ssdp_ipv4(self):
        payload = "M-SEARCH * HTTP/1.1\r\n" \
        "Host: 239.255.255.250:1900\r\n" \
        "ST: upnp:rootdevice\r\n" \
        "Man:\"ssdp:discover\"\r\n" \
        "MX:1\r\n\r\n" \

        ssdpRequest = IP(src=SRC_IP_V4,dst="239.255.255.250") / UDP(sport=1900, dport=1900) / payload
        send(ssdpRequest)

#############
# IPv6 SSDP #
#############

    #dstは"ff02::c"で固定
    #sport、dportは1900で固定
    def ssdp_ipv6(self):
        payload = "M-SEARCH * HTTP/1.1\r\n" \
        "Host: [FF02::C]:1900\r\n" \
        "ST: upnp:rootdevice\r\n" \
        "Man:\"ssdp:discover\"\r\n" \
        "MX:3\r\n\r\n" \

        ssdpRequest = IPv6(src=SRC_IP_V6,dst="ff02::c") / UDP(sport=1900, dport=1900) / payload
        send(ssdpRequest)

#####################
# IPv4 WS-Discovery #
#####################

    #dstは"239.255.255.250"で固定
    #dportは3702で固定
    #一度返答があると暫く応答をしてくれなくなるので二回目以降は少し時間をあけてから実施すること
    #WireSharkでパケットを見る際は "UDP" でフィルタリングする
    def wsdiscovery_ipv4(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+uuid+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IP(src=SRC_IP_V4,dst='239.255.255.250') / UDP(sport=53960, dport=3702) / payload
        send(pkt)

#####################
# IPv6 WS-Discovery #
#####################

    #dstは"ff02::c"で固定
    #dportは3702で固定
    #一度返答があると暫く応答をしてくれなくなるので二回目以降は少し時間をあけてから実施すること
    #WireSharkでパケットを見る際は "UDP" でフィルタリングする
    def wsdiscovery_ipv6(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+uuid+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IPv6(dst="ff02::c") / UDP(sport=53960, dport=3702) / payload
        sendp(pkt)

######################
# IPv4 mDNS(Bonjour) #
######################

    #dstは"224.0.0.251"で固定
    #sport、dportは5353で固定
    def mdns_ipv4(self):
        pkt = IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=NAME+".local", qtype='A'))
        send(pkt)

######################
# IPv6 mDNS(Bonjour) #
######################

    #dstは"ff02::fb"で固定
    #sport、dportは5353で固定
    def mdns_ipv6(self):
        pkt = IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=NAME+".local", qtype='A'))
        send(pkt)

#-------------------------------------------------------------------------------

################
# IPv6 TCP ALL #
################

    #dportは必ず空いているポートに固定
    def ipv6_tcp_all(self):
        for ip in DST_IP:
            pkt = IPv6(src=SRC_IP_V6, dst=ip) / TCP(dport=5355)
            send(pkt)

##########################
# IPv6 TCP Manual Adress #
##########################

    #dportは必ず空いているポートに固定
    def ipv6_tcp_manual(self):
        pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[0]) / TCP(dport=5355)
        send(pkt)

#############################
# IPv6 TCP Linklocal Adress #
#############################

    #dportは必ず空いているポートに固定
    def ipv6_tcp_linklocal(self):
        pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[1]) / TCP(dport=5355)
        send(pkt)

#################
# IPv6 TCP DHCP #
#################

    #dportは必ず空いているポートに固定
    def ipv6_tcp_dhcp(self):
        pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[2]) / TCP(dport=5355)
        send(pkt)

################################
# IPv6 TCP Stateless Adresses #
################################

    #dportは必ず空いているポートに固定
    def ipv6_tcp_stateless(self, num):
        length = len(DST_IP)
        number = num + 1
        if length < number:
            print("\nアドレスが設定されていません")
            num = input("\nPress Enter Key")
            tests.ipv6_TCP()
        else:
            pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[num]) / TCP(dport=5355)
            send(pkt)

################
# IPv6 UDP ALL #
################

    #dportは必ず空いているポートに固定
    def ipv6_udp_all(self):
        for ip in DST_IP:
            pkt = IPv6(src=SRC_IP_V6, dst=ip) / UDP(dport=5355)
            send(pkt)

##########################
# IPv6 UDP Manual Adress #
##########################

    #dportは必ず空いているポートに固定
    def ipv6_udp_manual(self):
        pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[0]) / UDP(dport=5355)
        send(pkt)

#############################
# IPv6 UDP Linklocal Adress #
#############################

    #dportは必ず空いているポートに固定
    def ipv6_udp_linklocal(self):
        pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[1]) / UDP(dport=5355)
        send(pkt)

#################
# IPv6 UDP DHCP #
#################

    #dportは必ず空いているポートに固定
    def ipv6_udp_dhcp(self):
        pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[2]) / UDP(dport=5355)
        send(pkt)

################################
# IPv6 UDP Stateless Adresses #
################################

    #dportは必ず空いているポートに固定
    def ipv6_udp_stateless(self, num):
        length = len(DST_IP)
        number = num + 1
        if length < number:
            print("\nアドレスが設定されていません")
            num = input("\nPress Enter Key")
            tests.ipv6_UDP()
        else:
            pkt = IPv6(src=SRC_IP_V6, dst=DST_IP[num]) / UDP(dport=5355)
            send(pkt)

tests = Tests()
tests.run()
