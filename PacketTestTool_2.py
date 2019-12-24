#Scapy Version:2.4.0
#Python Version:3.7.2
#作成日：2019/09/11
#作成者：笈川 萌


########
# 注意 #
########

# 1. テストプログラムを動かすPCのファイアウォールの設定を確認しておくこと（対象のパケットの送受信を行うには規則を「有効」にしておく必要がある）
# 2. "run_scapy"を実行してからテストプログラムを動かすこと
# 3. scapy-2.4.0\scapy\fields.py の NetBIOSNAMEField を修正してからテストプログラムを動かすこと

#    <修正前>   x = b"".join(chb(0x41 + orb(b)>>4) + chb(0x41 + orb(b)&0xf) for b in x)
#
#                                        括弧を追加                 括弧を追加
#    <修正後>   x = b"".join(chb(0x41 + (orb(b)>>4)) + chb(0x41 + (orb(b)&0xf)) for b in x)



from scapy.all import *

###################################
# 実機に合わせて以下を変更して下さい #
###################################

IFACE = "BUFFALO LUA2/3-U2-ATX Fast Ethernet Adapter"                #Windowsで狙ったinterfaceにパケットを出す（run_scapyをしたところで"IFACES"と叩く）

DST_IP_V4 = "192.168.10.101"                                         #送信先のIPv4アドレスを記入
DST_IP_V6 = "fe80:0000:0000:0000:0226:73ff:fe04:1fcb"                #送信先のIPv6アドレスを記入

SRC_IP_V4 = "192.168.10.103"                                         #送信元のIPv4アドレスを記入
SRC_IP_V6 = "fe80::d1de:b60:e26b:f9f5"                               #送信元のIPv6アドレスを記入

N_NAME = "TEST01<00>"                                                #ecology.ini の NetBIOS Name Service名前情報 と同じようにする
L_NAME = "test01"                                                    #ecology.ini の LLMNR名前情報 と同じようにする
B_NAME = "HOSTNAME.local"                                            #ecology.ini の Bonjour名前情報 と同じようにする(xxx.local の x 部分は大文字で記載すること)

UUID = 'bf6774d2-3e64-11e8-aca3-8662aadcadfa'                        #送信先のUUIDを記入(シングルクォーテーションで記入すること)



class Snmp:


#<SNMP>
#dportは161で固定

    # SNMP analyze_pkt snmp_tab Err IPv4 
    def SNMP_analyze_pkt_snmp_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[42] = 29
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt snmp_tab Err IPv6 
    def SNMP_analyze_pkt_snmp_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[42+20] = 29
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt snmp_length Err IPv4 
    def SNMP_analyze_pkt_snmp_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[43] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt snmp_length Err IPv6 
    def SNMP_analyze_pkt_snmp_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[43+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP tlv_length too big IPv4 
    def SNMP_tlv_length_too_big_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[43] = 131
        sendp(ba,iface=IFACE)

    # SNMP tlv_length too big IPv6 
    def SNMP_tlv_length_too_big_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[43+20] = 131
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ver_tab Err IPv4 
    def SNMP_analyze_pkt_ver_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[44] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ver_tab Err IPv6
    def SNMP_analyze_pkt_ver_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[44+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ver_length Err IPv4
    def SNMP_analyze_pkt_ver_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[45] = 131
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ver_length Err IPv6
    def SNMP_analyze_pkt_ver_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[45+20] = 131
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt com_tab Err IPv4
    def SNMP_analyze_pkt_com_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[47] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt com_tab Err IPv6
    def SNMP_analyze_pkt_com_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[47+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt com_length Err IPv4
    def SNMP_analyze_pkt_com_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[48] = 131
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt com_length Err IPv6
    def SNMP_analyze_pkt_com_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[48+20] = 131
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt data_length Err IPv4
    def SNMP_analyze_pkt_data_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[56] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt data_length Err IPv6
    def SNMP_analyze_pkt_data_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[56+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt req_tab Err IPv4
    def SNMP_analyze_pkt_req_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[57] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt req_tab Err IPv6
    def SNMP_analyze_pkt_req_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[57+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt req_length Err IPv4
    def SNMP_analyze_pkt_req_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[58] = 131
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt req_length Err IPv6
    def SNMP_analyze_pkt_req_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[58+20] = 131
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ers_tab Err IPv4
    def SNMP_analyze_pkt_ers_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[60] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ers_tab Err IPv6
    def SNMP_analyze_pkt_ers_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[60+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ers_length Err IPv4
    def SNMP_analyze_pkt_ers_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[61] = 2
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ers_length Err IPv6
    def SNMP_analyze_pkt_ers_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[61+20] = 2
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt eri_tab Err IPv4
    def SNMP_analyze_pkt_eri_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[63] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt eri_tab Err IPv6
    def SNMP_analyze_pkt_eri_tab_Err_IPv6(self):
        pkt = Ether() /IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[63+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt eri_length Err IPv4
    def SNMP_analyze_pkt_eri_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[64] = 2
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt eri_length Err IPv6
    def SNMP_analyze_pkt_eri_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[64+20] = 2
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vbl_tab Err IPv4
    def SNMP_analyze_pkt_vbl_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[66] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vbl_tab Err IPv6
    def SNMP_analyze_pkt_vbl_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[66+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vbl_length Err IPv4
    def SNMP_analyze_pkt_vbl_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[67] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vbl_length Err IPv6
    def SNMP_analyze_pkt_vbl_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[67+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vb_tab Err IPv4
    def SNMP_analyze_pkt_vb_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[68] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vb_tab Err IPv6
    def SNMP_analyze_pkt_vb_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[68+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vb_length Err IPv4
    def SNMP_analyze_pkt_vb_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[69] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt vb_length Err IPv6
    def SNMP_analyze_pkt_vb_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[69+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ot_tab Err IPv4
    def SNMP_analyze_pkt_ot_tab_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[70] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ot_tab Err IPv6
    def SNMP_analyze_pkt_ot_tab_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[70+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ot_length Err IPv4
    def SNMP_analyze_pkt_ot_length_Err_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[71] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ot_length Err IPv6
    def SNMP_analyze_pkt_ot_length_Err_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[71+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ov_tab Wrn IPv4 <警告> 
    def SNMP_analyze_pkt_ov_tab_Wrn_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[81] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ov_tab Wrn IPv6 <警告>
    def SNMP_analyze_pkt_ov_tab_Wrn_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[81+20] = 0
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ov_length Wrn IPv4 <警告>
    def SNMP_analyze_pkt_ov_length_Wrn_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[82] = 2
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt ov_length Wrn IPv6 <警告>
    def SNMP_analyze_pkt_ov_length_Wrn_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[82+20] = 2
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt OverRun IPv4
    def SNMP_analyze_pkt_OverRun_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[82] = 2
        sendp(ba,iface=IFACE)

    # SNMP analyze_pkt OverRun IPv6
    def SNMP_analyze_pkt_OverRun_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[82+20] = 2
        sendp(ba,iface=IFACE)

    # Rec=IPv4 UDP SNMP OK
    def SNMP_Go_Main_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("43.6.1.2.1.25.3.2.1.5.1"))]))
        sendp(pkt,iface=IFACE)

    # Rec=IPv6 UDP SNMP OK
    def SNMP_Go_Main_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("43.6.1.2.1.25.3.2.1.5.1"))]))
        sendp(pkt,iface=IFACE)



class Llmnr:

    #<LLMNR>
    #dstは"224.0.0.252"で固定
    #dportは5355で固定

    # LLMNR Question Section Name No match IPv4
    def LLMNR_Question_Section_Name_No_match_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname="aaaaa"))
        sendp(pkt,iface=IFACE)

    # LLMNR Question Section Name No match IPv6
    def LLMNR_Question_Section_Name_No_match_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname="aaaaa",qtype=28))
        sendp(pkt,iface=IFACE)

    # LLMNR Question Section Name Complession IPv4
    def LLMNR_Question_Section_Name_Complession_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[54] = 192
        sendp(ba,iface=IFACE)

    # LLMNR Question Section Name Complession IPv6
    def LLMNR_Question_Section_Name_Complession_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[54+20] = 192
        sendp(ba,iface=IFACE)

    # LLMNR Question Section len bit(%x) Not 0 IPv4
    def LLMNR_Question_Section_len_bit_x_Not_0_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[54] = 99
        sendp(ba,iface=IFACE)

    # LLMNR Question Section len bit(%x) Not 0 IPv6
    def LLMNR_Question_Section_len_bit_x_Not_0_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[54+20] = 99
        sendp(ba,iface=IFACE)

    # LLMNR Question Section Abnormal Len IPv4
    def LLMNR_Question_Section_Abnormal_Len_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[54] = 1
        sendp(ba,iface=IFACE)

    # LLMNR Question Section Abnormal Len IPv6
    def LLMNR_Question_Section_Abnormal_Len_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[54+20] = 1
        sendp(ba,iface=IFACE)

    # LLMNR Question Section QTYPE(%x) Err IPv4
    def LLMNR_Question_Section_QTYPE_x_Err_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[63] = 255
        sendp(ba,iface=IFACE)

    # LLMNR Question Section QTYPE(%x) Err IPv6 
    def LLMNR_Question_Section_QTYPE_x_Err_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[63+20] = 255
        sendp(ba,iface=IFACE)

    # LLMNR Question Section QTYPE(%x) But IPv4 Disable <注意> ecology.ini の ip_version を MS_IFLT_IPVER_6 にしておくこと
    def LLMNR_Question_Section_QTYPE_x_But_IPv4_Disable(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[63+20] = 1
        sendp(pkt,iface=IFACE)

    # LLMNR Question Section QTYPE(%x) But IPv6 Disable <注意> ecology.ini の ip_version を MS_IFLT_IPVER_4 にしておくこと
    def LLMNR_Question_Section_QTYPE_x_But_IPv6_Disable(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[63] = 28
        sendp(ba,iface=IFACE)

    # LLMNR Question Section QCLASS(%x) Err IPv4
    def LLMNR_Question_Section_QCLASS_x_Err_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[64] = 255
        ba[65] = 255
        sendp(ba,iface=IFACE)

    # LLMNR Question Section QCLASS(%x) Err IPv6
    def LLMNR_Question_Section_QCLASS_x_Err_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[64+20] = 255
        ba[65+20] = 255
        sendp(ba,iface=IFACE)

    # LLMNR Question Section Flag(%x) Not 0 IPv4
    def LLMNR_Question_Section_Flag_x_Not_0_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[45] = 255
        sendp(ba,iface=IFACE)

    # LLMNR Question Section Flag(%x) Not 0 IPv6
    def LLMNR_Question_Section_Flag_x_Not_0_IPv6s(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[45+20] = 255
        sendp(ba,iface=IFACE)

    # LLMNR Question Section QDCOUNT(%x) Not 1 IPv4
    def LLMNR_Question_Section_QDCOUNT_x_Not_1_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[47] = 255
        sendp(ba,iface=IFACE)

    # LLMNR Question Section QDCOUNT(%x) Not 1 IPv6
    def LLMNR_Question_Section_QDCOUNT_x_Not_1_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[47+20] = 255
        sendp(ba,iface=IFACE)

    # Send IPv4 LLMNR Rep
    def Send_IPv4_LLMNR_Rep(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        sendp(pkt,iface=IFACE)

    # Send IPv6 LLMNR Rep
    def Send_IPv6_LLMNR_Rep(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        sendp(pkt,iface=IFACE)

    # Des=IPv4 LLMNR <注意> ecology.ini の LLMNR有効/無効フラグ を MS_IFLT_LLMNR_DISABLE にしておくこと
    def Des_IPv4_LLMNR(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        sendp(pkt,iface=IFACE)

    # Des=IPv6 LLMNR <注意> ecology.ini の LLMNR有効/無効フラグ を MS_IFLT_LLMNR_DISABLE にしておくこと
    def Des_IPv6_LLMNR(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME,qtype=28))
        sendp(pkt,iface=IFACE)



class Nbns:

    # <NBNS>
    #dstは"192.168.10.255"で固定
    #sport、dportは137で固定

    # NBNS Response Flag(%x) Not 0
    def NBNS_Response_Flag_x_Not_0(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[44] = 255
        sendp(ba,iface=IFACE)

    # NBNS Name Len(%x) Not 0x%x
    def NBNS_Name_Len_x_Not_0x_x(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[54] = 0
        sendp(ba,iface=IFACE)

    # Node Status Resource Record
    def Node_Status_Resource_Record(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[89] = 33
        sendp(ba,iface=IFACE)

    # NBNS QTYPE(%x) Not 0x%x
    def NBNS_QTYPE_x_Not_0x_x(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[89] = 255
        sendp(ba,iface=IFACE)

    # NBNS QCLASS(%x) Not 0x%x
    def NBNS_QCLASS_x_Not_0x_x(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[90] = 255
        ba[91] = 255
        sendp(ba,iface=IFACE)

    # NBNS Name No match
    def NBNS_Name_No_match(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME="aaa")
        sendp(pkt,iface=IFACE)

    # NBNS RCODE(%x) Not 0
    def NBNS_RCODE_x_Not_0(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[45] = 255
        sendp(ba,iface=IFACE)

    # NBNS Flag Section Err
    def NBNS_Flag_Section_Err(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[45] = 15
        sendp(ba,iface=IFACE)

    # NBNS QDCOUNT(%x) Not 1
    def NBNS_QDCOUNT_x_Not_1(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,QDCOUNT=2,ANCOUNT=1,NSCOUNT=1,ARCOUNT=1,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        sendp(pkt,iface=IFACE)

    # Send IPv4 NetBIOS Name Service Rep
    def Send_IPv4_NetBIOS_Name_Service_Rep(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,QDCOUNT=1,ANCOUNT=1,NSCOUNT=1,ARCOUNT=1,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        sendp(pkt,iface=IFACE)

    # NBNS Multi-Homed Name Registration メイン復帰させる
    def NBNS_Multi_Homed_Name_Registration(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[44] = 127
        ba[45] = 255
        sendp(ba,iface=IFACE)

    # NBNS Registration メイン復帰させる
    def NBNS_Registration(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        b = bytes(pkt)
        ba = bytearray(b)
        ba[44] = 40
        ba[45] = 255
        sendp(ba,iface=IFACE)

    # Des=IPv4 NetBIOS <注意> ecology.ini の NetBIOS有効/無効フラグ を MS_IFLT_NETBIOS_DISABLE にしておくこと
    def Des_IPv4_NetBIOS(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="192.168.10.255")/ UDP(sport=137,dport=137) / NBNSQueryRequest(NAME_TRN_ID=0xfffb,SUFFIX="workstation",QUESTION_NAME=N_NAME)
        sendp(pkt,iface=IFACE)



class Mdns:

    # <mDNS>
    #dst(IPv4)は"224.0.0.251"で固定
    #dst(IPv6)は"ff02::fb"で固定
    #sport、dportは5353で固定

    # IFI_MDNS_MSD_RES(1)レスポンスパケット(破棄) IPv4 -> IFI:mDNS - Stay at STR(ret=1)
    def mDNS_Stay_at_STR_1_IPv4(self):
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[44] = 255
        sendp(ba,iface=IFACE)

    # IFI_MDNS_MSD_RES(1)レスポンスパケット(破棄) IPv6 -> IFI:mDNS - Stay at STR(ret=1)
    def mDNS_Stay_at_STR_1_IPv6(self):
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[44+20] = 255
        sendp(ba,iface=IFACE)
        
    # IFI_MDNS_UNMATCH_ADDR4(2) アドレス不一致v4(破棄) IPv4 -> IFI:mDNS - Stay at STR(ret=2)
    def mDNS_Stay_at_STR_2_IPv4(self):
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="192.168.1.10.in-addr.arpa.",qtype="PTR"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_UNMATCH_ADDR4(2) アドレス不一致v4 IPv6 -> IFI:mDNS - Stay at STR(ret=2)
    def mDNS_Stay_at_STR_2_IPv6(self):
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="192.168.1.10.in-addr.arpa.",qtype="PTR"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_UNMATCH_ADDR6(3) アドレス不一致v6(破棄) IPv4 -> IFI:mDNS - Stay at STR(ret=3)
    def mDNS_Stay_at_STR_3_IPv4(self):
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.ip6.arpa.",qtype="PTR"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_UNMATCH_ADDR6(3) アドレス不一致v6(破棄) IPv6 -> IFI:mDNS - Stay at STR(ret=3)
    def mDNS_Stay_at_STR_3_IPv6(self):
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.ip6.arpa.",qtype="PTR"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_UNMATCH_SRV(4) サービス名不一致(破棄) IPv4 -> IFI:mDNS - Stay at STR(ret=4)
    def mDNS_Stay_at_STR_4_IPv4(self):
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="aaa.local", qtype="PTR"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_UNMATCH_SRV(4) サービス名不一致(破棄) IPv6 -> IFI:mDNS - Stay at STR(ret=4)
    def mDNS_Stay_at_STR_4_IPv6(self):
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="aaa.local", qtype="PTR"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_UNMATCH_NAME(5) QNAME不一致(破棄)(Rcv:%s) IPv4 -> IFI:mDNS - Stay at STR(ret=5) 
    def mDNS_Stay_at_STR_5_IPv4(self):
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="aaa.local", qtype="A"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_UNMATCH_NAME(5) QNAME不一致(破棄)(Rcv:%s) IPv6 -> IFI:mDNS - Stay at STR(ret=5)
    def mDNS_Stay_at_STR_5_IPv6(self): 
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname="aaa.local", qtype="A"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_PACKET_ERR(6) パケット構文エラー(破棄) IPv4 -> IFI:mDNS - Stay at STR(ret=6)
    def mDNS_Stay_at_STR_6_IPv4(self): 
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[47] = 0
        sendp(ba,iface=IFACE)

    # IFI_MDNS_PACKET_ERR(6) パケット構文エラー(破棄) IPv6 -> IFI:mDNS - Stay at STR(ret=6)
    def mDNS_Stay_at_STR_6_IPv6(self): 
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        b = bytes(pkt)
        ba = bytearray(b)
        ba[47+20] = 0
        sendp(ba,iface=IFACE)

    # IFI_MDNS_ANALYZE_ERR(7) パケット解析エラー(破棄) IPv4 -> IFI:mDNS - Stay at STR(ret=7) <注意> ecology.ini の Bonjour名前情報 を全てコメントアウトしておくこと
    def mDNS_Stay_at_STR_7_IPv4(self): 
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        sendp(pkt,iface=IFACE)

    # IFI_MDNS_ANALYZE_ERR(7) パケット解析エラー(破棄) IPv6 -> IFI:mDNS - Stay at STR(ret=7) <注意> ecology.ini の Bonjour名前情報 を全てコメントアウトしておくこと
    def mDNS_Stay_at_STR_7_IPv6(self): 
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        sendp(pkt,iface=IFACE)

    # mDNS - Return from STR(ptn=%d) IPv4 メイン復帰させる
    def mDNS_Return_from_STR_IPv4(self):
        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        sendp(pkt,iface=IFACE)

    # mDNS - Return from STR(ptn=%d) IPv6 メイン復帰させる
    def mDNS_Return_from_STR_IPv6(self):
        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=B_NAME, qtype="A"))
        sendp(pkt,iface=IFACE)

    # mDNS - QNAME buffer over!! IPv4
    def mDNS_QNAME_buffer_over_IPv4(self):
        d_qname = "a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a"

        pkt = Ether() / IP(dst="224.0.0.251") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=d_qname + ".ip6.arpa.",qtype="PTR"))
        sendp(pkt,iface=IFACE)

    # mDNS - QNAME buffer over!! IPv6
    def mDNS_QNAME_buffer_over_IPv6(self):
        d_qname = "a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.\
                   a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a"

        pkt = Ether() / IPv6(dst="ff02::fb") / UDP(sport=5353,dport=5353) / DNS(rd=1,qd=DNSQR(qname=d_qname + ".ip6.arpa.",qtype="PTR"))
        sendp(pkt,iface=IFACE)



class Ssdp:
    
    # <SSDP>
    #dst(IPv4)は"239.255.255.250"で固定
    #dst(IPv6)は"ff02::fb"で固定
    #sport、dportは1900で固定

    # IFI_SSDP_UNMATCH_METHOD(1) メソッド不一致(破棄) IPv4 -> SSDP - Stay at STR(ret=1)
    def SSDP_Stay_at_STR_1_IPv4(self):
        payload1 = "M-SEARCHO * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: upnp:rootdevice\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IP(src=SRC_IP_V4,dst="239.255.255.250") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)

    # IFI_SSDP_UNMATCH_METHOD(1) メソッド不一致(破棄) IPv6 -> SSDP - Stay at STR(ret=1)
    def SSDP_Stay_at_STR_1_IPv6(self):
        payload1 = "M-SEARCHO * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: upnp:rootdevice\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IPv6(src=SRC_IP_V6,dst="ff02::fb") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)

    # IFI_SSDP_NO_ST(2) STフィールド無し(破棄) IPv4 -> IFI:SSDP - Stay at STR(ret=2)
    def SSDP_Stay_at_STR_2_IPv4(self):
        payload1 = "M-SEARCH * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: \r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IP(src=SRC_IP_V4,dst="239.255.255.250") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)

    # IFI_SSDP_NO_ST(2) STフィールド無し(破棄) IPv6 -> IFI:SSDP - Stay at STR(ret=2)
    def SSDP_Stay_at_STR_2_IPv6(self):
        payload1 = "M-SEARCH * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: \r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IPv6(src=SRC_IP_V6,dst="ff02::fb") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)

    # IFI_SSDP_UNMATCH_ST(3) ST不一致(破棄) IPv4 -> IFI:SSDP - Stay at STR(ret=3)
    def SSDP_Stay_at_STR_3_IPv4(self):
        payload1 = "M-SEARCH * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: aaa\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IP(src=SRC_IP_V4,dst="239.255.255.250") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)

    # IFI_SSDP_UNMATCH_ST(3) ST不一致(破棄) IPv6 -> IFI:SSDP - Stay at STR(ret=3)
    def SSDP_Stay_at_STR_3_IPv6(self):
        payload1 = "M-SEARCH * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: aaa\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IPv6(src=SRC_IP_V6,dst="ff02::fb") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)

    # IFI_SSDP_PACKET_ERR(4) UDPデータ長エラー(破棄) IPv4 -> IFI:SSDP - Stay at STR(ret=4)
    def SSDP_Stay_at_STR_4_IPv4(self):
        payload1 = "M-SEARCH * HTTP/1.\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: upnp:rootdevice\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IP(src=SRC_IP_V4,dst="239.255.255.250") / UDP(sport=1900, dport=1900) / payload1
        send(ssdpRequest,iface=IFACE)

    # IFI_SSDP_PACKET_ERR(4) UDPデータ長エラー(破棄) IPv6 -> IFI:SSDP - Stay at STR(ret=4)
    def SSDP_Stay_at_STR_4_IPv6(self):
        payload1 = "M-SEARCH * HTTP/1.\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: upnp:rootdevice\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IPv6(src=SRC_IP_V6,dst="ff02::fb") / UDP(sport=1900, dport=1900) / payload1
        send(ssdpRequest,iface=IFACE)

    # IFI:SSDP - Return from STR(ptn=%d) IPv4 メイン復帰させる
    def SSDP_Return_from_STR_IPv4(self):
        payload1 = "M-SEARCH * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: upnp:rootdevice\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IP(src=SRC_IP_V4,dst="239.255.255.250") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)

    # IFI:SSDP - Return from STR(ptn=%d) IPv6 メイン復帰させる
    def SSDP_Return_from_STR_IPv6(self):
        payload1 = "M-SEARCH * HTTP/1.1\r\n"
        payload2 = "Host: 239.255.255.250:1900\r\n"
        payload3 = "ST: upnp:rootdevice\r\n"
        payload4 = "Man:\"ssdp:discover\"\r\n"
        payload5 = "MX:1\r\n\r\n"

        ssdpRequest = IPv6(src=SRC_IP_V6,dst="ff02::fb") / UDP(sport=1900, dport=1900) / (payload1 + payload2 + payload3 + payload4 + payload5)
        send(ssdpRequest,iface=IFACE)



class Ws_discovery:
    
    # WS-Discovery

        #dstは"239.255.255.250"で固定
        #dportは3702で固定
        #一度返答があると暫く応答をしてくれなくなるので二回目以降は少し時間をあけてから実施すること
        #WireSharkでパケットを見る際は "UDP" でフィルタリングする


    # IFI_WSD_UNMATCH_TAG(1) タグ不一致(破棄) IPv4 -> IFI:WSDD - Stay at STR(ret=1)
    def WSDD_Stay_at_STR_1_IPv4(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IP(dst='239.255.255.250') / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_UNMATCH_TAG(1) タグ不一致(破棄) IPv6 -> IFI:WSDD - Stay at STR(ret=1)
    def WSDD_Stay_at_STR_1_IPv6(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IPv6(dst="ff02::c") / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_UNMATCH_TYPE(2) タイプ不一致(破棄) IPv4 -> IFI:WSDD - Stay at STR(ret=2)
    def WSDD_Stay_at_STR_2_IPv4(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/Probe</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IP(dst='239.255.255.250') / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_UNMATCH_TYPE(2) タイプ不一致(破棄) IPv6 -> IFI:WSDD - Stay at STR(ret=2)
    def WSDD_Stay_at_STR_2_IPv6(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/Probe</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IPv6(dst="ff02::c") / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_UNMATCH_MSG(3) メッセージ種別不一致(破棄) IPv4 -> IFI:WSDD - Stay at STR(ret=3)
    def WSDD_Stay_at_STR_3_IPv4(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Hello</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IP(dst='239.255.255.250') / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_UNMATCH_MSG(3) メッセージ種別不一致(破棄) IPv6 -> IFI:WSDD - Stay at STR(ret=3)
    def WSDD_Stay_at_STR_3_IPv6(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Hello</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IPv6(dst="ff02::c") / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_UNMATCH_UUID(4) UUID不一致(破棄) IPv4 -> IFI:WSDD - Stay at STR(ret=4)
    def WSDD_Stay_at_STR_4_IPv4(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Resolve</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:aaa</wsa:MessageID></soap:Header><soap:Body><a:Address>uuid:aaa</a:Address><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IP(dst='239.255.255.250') / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_UNMATCH_UUID(4) UUID不一致(破棄) IPv6 -> IFI:WSDD - Stay at STR(ret=4)
    def WSDD_Stay_at_STR_4_IPv6(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Resolve</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:aaa</wsa:MessageID></soap:Header><soap:Body><a:Address>uuid:aaa</a:Address><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IPv6(dst="ff02::c") / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_PACKET_ERR(5) パケット構文エラー(破棄) IPv4 -> IFI:WSDD - Stay at STR(ret=5)
    def WSDD_Stay_at_STR_5_IPv4(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Resolve</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IP(dst='239.255.255.250') / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # IFI_WSD_PACKET_ERR(5) パケット構文エラー(破棄) IPv6 -> IFI:WSDD - Stay at STR(ret=5)
    def WSDD_Stay_at_STR_5_IPv6(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Resolve</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IPv6(dst="ff02::c") / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # WSDD - Return from STR(ptn=%d) IPv4
    def WSDD_Return_from_STR_IPv4(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IP(dst='239.255.255.250') / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)

    # WSDD - Return from STR(ptn=%d) IPv6
    def WSDD_Return_from_STR_IPv6(self):
        payload = '<?xml version="1.0" encoding="utf-8" ?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"'\
                  'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery"'\
                  'xmlns:wsdp="http://schemas.xmlsoap.org/ws/2006/02/devprof"><soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery'\
                  '</wsa:To><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action><wsa:MessageID>'\
                  'urn:UUID:'+UUID+'</wsa:MessageID></soap:Header><soap:Body><wsd:Probe><wsd:Types>wsdp:Device</wsd:Types>'\
                  '</wsd:Probe></soap:Body></soap:Envelope>'\

        pkt = Ether() / IPv6(dst="ff02::c") / UDP(sport=53960, dport=3702) / payload
        sendp(pkt,iface=IFACE)



class Icmp:
    
    # <ICMP>

    # ICMPv4 Echo Rep
    def ICMP_Echo_Rep_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4) / ICMP()
        sendp(pkt,iface=IFACE)

    # ICMPv4 Not Echo Rep
    def ICMP_Not_Echo_Rep_IPv4(self):
        pkt = Ether() / IP(dst=DST_IP_V4) / ICMP(type=3, code=1)
        sendp(pkt,iface=IFACE)

    # ARP Reply
    def ARP(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=DST_IP_V4)
        sendp(pkt,iface=IFACE)

    # ICMPv6 Echo Rep
    def ICMP_Echo_Rep_IPv6(self):
        pkt = Ether() / IPv6(dst=DST_IP_V6) / ICMPv6EchoRequest()
        sendp(pkt,iface=IFACE)

    # ICMPv6 Not for me
    def ICMP_Not_for_me_IPv6(self):
        pkt = Ether() / IPv6(dst="fe80:0000:0000:0000:0226:73ff:fe04:0000") / ICMPv6EchoRequest()
        sendp(pkt,iface=IFACE)

    # Dst Address No Register Multicast Address
    def Dst_Address_No_Register_Multicast_Address(self):
        pkt = IPv6(dst="fe80:0000:0000:0000:0226:73ff:fe04:0000",hlim=1) /IPv6ExtHdrHopByHop() / ICMPv6MLQuery()
        send(pkt,iface=IFACE)

    # MLQ General Query
    def MLQ_General_Query(self):
        pkt = IPv6(dst="ff02:0000:0000:0000:0000:0000:0000:0001",hlim=1) /IPv6ExtHdrHopByHop() / ICMPv6MLQuery()
        send(pkt,iface=IFACE)

    # Not Found Solicited Node Multicast Address!!! ※ ecology.iniのマルチキャストアドレス(最後が"c1"になっているもの)を"c2"に変更する
    def Not_Found_Solicited_Node_Multicast_Address(self):
        pkt = IPv6(dst="ff02:0000:0000:0000:0000:0000:0000:0001",hlim=1) /IPv6ExtHdrHopByHop() / ICMPv6MLQuery(mladdr="ff02:0000:0000:0000:0000:0000:0000:0001")
        send(pkt,iface=IFACE)

    # MLQ Multicast Address Not Register
    def MLQ_Multicast_Address_Not_Register(self):
        pkt = IPv6(dst="ff02:0000:0000:0000:0000:0000:0000:0001",hlim=1) /IPv6ExtHdrHopByHop() / ICMPv6MLQuery(mladdr="ff02:0000:0000:0000:0000:0000:0000:0000")
        send(pkt,iface=IFACE)

    # MLQ Multicast Address
    # Solicited Node Multicast Address Found
    def Solicited_Node_Multicast_Address_Found(self):
        pkt = IPv6(src="ff02:0000:0000:0000:0000:0000:1100:0001",dst="ff02:0000:0000:0000:0000:0000:0000:0001",hlim=1) /IPv6ExtHdrHopByHop() / ICMPv6MLQuery(mladdr="ff02:0000:0000:0000:0000:0000:0000:0001")
        send(pkt,iface=IFACE)



class Others:
    
    # IFILTER_acl_v4 Disable <注意> ecology.ini の IPv4アクセスコントロール情報 を全てコメントアウトしておくこと
    def IFILTER_acl_Disable_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        sendp(pkt,iface=IFACE)

    # IFILTER_acl_v6 Disable <注意> ecology.ini の IPv6アクセスコントロール情報 を全てコメントアウトしておくこと
    def IFILTER_acl_Disable_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        sendp(pkt,iface=IFACE)

    # IFILTER_acl_v4 範囲外  <注意> ecology.ini の IPv4アクセスコントロール情報 を範囲外になるように設定する（例）addr_min_v4=00:00:00:00, addr_max_v4=11:11:11:11
    def IFILTER_acl_Out_Of_Range_IPv4(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src=SRC_IP_V4,dst="224.0.0.252")/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        sendp(pkt,iface=IFACE)

    # IFILTER_acl_v6 範囲外  <注意> ecology.ini の IPv6アクセスコントロール情報 を範囲外になるように設定する（例）addr_min_v6=0000::00, addr_max_v6=1111::11
    def IFILTER_acl_Out_Of_Range_IPv6(self):
        pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / IPv6(src=SRC_IP_V6,dst=DST_IP_V6)/ UDP(sport=45345,dport=5355) /LLMNRQuery(id=RandShort(), qd=DNSQR(qname=L_NAME))
        sendp(pkt,iface=IFACE)

    #dportは161で固定(70パケット連続受信用)
    def snmp_ipv4_70(self):
        p = Ether(dst="58:38:79:0f:d0:42") / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        for i in range(70): 
            sendp(p,iface=IFACE)

    #dportは161で固定(90パケット連続受信用)
    def snmp_ipv4_90(self):
        p = Ether(dst="58:38:79:0f:d0:42") / IP(dst=DST_IP_V4)/UDP(dport=161)/SNMP(version=0,community="public",PDU=SNMPnext(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.4.1.2699.1.2"))]))
        for i in range(90): 
            sendp(p,iface=IFACE)



while True:
	print("")
	print("1.  SNMP")
	print("2.  LLMNR")
	print("3.  NBNS")
	print("4.  mDNS")
	print("5.  SSDP")
	print("6.  WS-Discovery")
	print("7.  ICMP")
	print("8.  Others")
	print("")
	num = input("Choose The Test: ").rstrip()
	if num == "1":
	    tests = Snmp()
	elif num == "2":
	    tests = Llmnr()
	elif num == "3":
	    tests = Nbns()
	elif num == "4":
	    tests = Mdns()
	elif num == "5":
	    tests = Ssdp()
	elif num == "6":
	    tests = Ws_discovery()
	elif num == "7":
	    tests = Icmp()
	elif num == "8":
	    tests = Others()
	else: 
	    exit()

	while True:
		#
		# 番号付き関数一覧を作成して、指定された関数を実行
		#

		func_list = []
		i = 1
		for func_name in dir(tests):
			if not str(func_name).startswith("_"):
				print(str(i) + " : " + func_name)
				func_list.append(str(func_name))
				i += 1

		num = int(input("Choose The Test number : ").rstrip())
		if(num >= 1 and num < i):
			print(func_list[num - 1])
			eval("tests." + str(func_list[num - 1]))()
		else:
			break





