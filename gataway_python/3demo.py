#!/usr/bin/python
#-*- encoding: utf-8 -*-
from M2Crypto.EVP import Cipher

'加密'
def encrypt_3des(key, text):
    encryptor = Cipher(alg='des_ede3_ecb', key=key, op=1, iv='\0' * 16)
    s = encryptor.update(text)
#    return s + encryptor.final()
    '返回十六进制数据, 并将字母变成大写'
    result_ = s + encryptor.final()
    result = (result_.encode('hex')).upper()
    return result
'''
解密
如果直接将encrypt_3des函数加密后的密文传进来需要将22行去掉,
22行的作用是将字符串数据转换成16进制字符串的形式,差别在与:
    假如字符串数据长度为8,转换之后的数据长度为4
'''
def decrypt_3des(key, text):
    text = str(bytearray.fromhex(text))
    decryptor = Cipher(alg='des_ede3_ecb', key=key, op=0, iv='\0' * 16)
    s = decryptor.update(text)
    return s + decryptor.final()


if __name__ == "__main__":
    key1 = "1469492616f9c6e175dfb1a8"
    text1 = "0AB7353E5C660209D111815F1E76B165C119DF5C611D2F4EE960C3D4481983AA83B4F777F6D3C4557C952CC52A7BB6808CDFF406DB48E4B1"
    text2 = '101#00003C33000B8149#02SB#6.1.1#000000#0021#02SB#06#'
    print encrypt_3des(key1, text2)
    print decrypt_3des(key1, text1)
'''
101#00003C33000B8149#02SB#6.1.1#000000#0021#02SB#06#
#zc#146949261600#0101#00003C33000B8149#02SB#6.1.1#000000#0021#02SB#06#
1469492616f9c6e175dfb1a8
#146949261600#0AB7353E5C660209D111815F1E76B165C119DF5C611D2F4EE960C3D4481983AA83B4F777F6D3C4557C952CC52A7BB6808CDFF406DB48E4B1

#zc#0101#0000000C29F0B7E8#0000#7.1.1#000000#0021#
14937066242f4b3d52614bef
#zc#149370662400#22B0A2F68BD7C52CE4AB6A79552D75047B9B73418E2083B1B31C5F6E5CB072ACF075D8ACDBC455B70A2B828A72B26D78


#149370661100#805132C86A26A0B6C2DAA684D18423A8B1CA0BC3EE3394B52AB9CEDEB2B8645D47A25B8F470BCB2B16B13AF1001743FD99D5B98B0D78F33C
1493706611 97F3B3C1FC8DA9
0101#0000000C29F0B7E8#0000#7.1.1#000000#0021#&f0#

#sz#0101#0000000C29F0B7E8#0000#7.1.1#000000#0022#
149370662522ee18fa074f15
#sz#149370662500#398DC2957FDD48F4B105C44013B7FC7761393BD711829F43F2C358FFD6EDDF3F683C5E3DCE3ADE5488CF02FEED804B45

'''