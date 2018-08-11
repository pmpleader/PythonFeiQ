#command
IPMSG_NOOPERATION = 0x00000000

IPMSG_BR_ENTRY = 0x00000001    #用户上线
IPMSG_BR_EXIT = 0x00000002#用户下线
IPMSG_ANSENTRY = 0x00000003#通报在线，回复【用户上线】
IPMSG_BR_ABSENCE = 0x00000004#通报离线模式取消或用户名变更

#下面这组不知道干嘛的
IPMSG_BR_ISGETLIST = 0x00000010
IPMSG_OKGETLIST = 0x00000011
IPMSG_GETLIST = 0x00000012
IPMSG_ANSLIST = 0x00000013
IPMSG_BR_ISGETLIST2 = 0x00000018

IPMSG_SENDMSG = 0x00000020#发送一条消息，如果发送者不认识，发送IPMSG_BR_ENTRY，但如果标记了IPMSG_NOADDLISTOPT，放过他
IPMSG_RECVMSG = 0x00000021#通知消息已经接收，仅当设置IPMSG_SENDCHECKOPT，附加区写入原始包序号
IPMSG_READMSG = 0x00000030#响应IPMSG_SECRETOPT+SENDMSG，附加区写入原始包序号
IPMSG_DELMSG = 0x00000031#
IPMSG_ANSREADMSG = 0x00000032#响应READMSG+READCHECKOPT

IPMSG_GETINFO = 0x00000040#请求ipmsg协议版本
IPMSG_SENDINFO = 0x00000041#发送ipmsg协议版本

IPMSG_GETABSENCEINFO = 0x00000050#请问你离线了吗？
IPMSG_SENDABSENCEINFO = 0x00000051#对啊，离线；Not absence mode没离线

IPMSG_GETFILEDATA = 0x00000060
IPMSG_RELEASEFILES = 0x00000061
IPMSG_GETDIRFILES = 0x00000062

IPMSG_GETPUBKEY = 0x00000072 #请求公钥
IPMSG_ANSPUBKEY = 0x00000073 #回复公钥

#飞秋的扩展协议
IPMSG_OPEN_YOU = 0x00000077#no extra
IPMSG_RESP_YOU = 0x00000078#no extra
IPMSG_INPUTING = 0x00000079#no extra。发送完消息也会跟一条，并且没有7a，why？
IPMSG_INPUT_END = 0x0000007a#no extra
IPMSG_KNOCK = 0x000000d1#窗口抖动

IPMSG_SENDIMAGE = 0x000000c0#发送图片
IPMSG_REPORT_RECVIMAGE = 0x000000c1  # 确认接收到图片报文

#option for all command
IPMSG_ABSENCEOPT = 0x00000100
IPMSG_SERVEROPT = 0x00000200
IPMSG_DIALUPOPT = 0x00010000
IPMSG_FILEATTACHOPT = 0x00200000
IPMSG_ENCRYPTOPT = 0x00400000
IPMSG_UTF8OPT = 0x00800000

#option for Send command
IPMSG_SENDCHECKOPT = 0x00000100
IPMSG_SECRETOPT = 0x00000200
IPMSG_BROADCASTOPT = 0x00000400
IPMSG_MULTICASTOPT = 0x00000800
IPMSG_NOPOPUPOPT = 0x00001000
IPMSG_AUTORETOPT = 0x00002000
IPMSG_RETRYOPT = 0x00004000
IPMSG_PASSWORDOPT = 0x00008000
IPMSG_NOLOGOPT = 0x00020000
IPMSG_NEWMUTIOPT = 0x00040000
IPMSG_NOADDLISTOPT = 0x00080000
IPMSG_READCHECKOPT = 0x00100000
IPMSG_SECRETEXOPT = (IPMSG_READCHECKOPT | IPMSG_SECRETOPT)

IPMSG_NO_REPLY_OPTS = (IPMSG_BROADCASTOPT | IPMSG_AUTORETOPT)

#encryption flags for encrypt command
IPMSG_RSA_512 = 0x00000001
IPMSG_RSA_1024 = 0x00000002
IPMSG_RSA_2048 = 0x00000004
IPMSG_RC2_40 = 0x00001000
IPMSG_RC2_128 = 0x00004000
IPMSG_RC2_256 = 0x00008000
IPMSG_BLOWFISH_128 = 0x00020000
IPMSG_BLOWFISH_256 = 0x00040000
IPMSG_AES_128 = 0x00100000
IPMSG_AES_192 = 0x00200000
IPMSG_AES_256 = 0x00400000
IPMSG_SIGN_STAMPOPT = 0x01000000
IPMSG_SIGN_MD5 = 0x10000000
IPMSG_SIGN_SHA1 = 0x20000000

#compatibilty for Win beta version
IPMSG_RC2_40OLD = 0x00000010   # for beta1-4 only
IPMSG_RC2_128OLD = 0x00000040   # for beta1-4 only
IPMSG_BLOWFISH_128OLD = 0x00000400   # for beta1-4 only
IPMSG_RC2_40ALL = (IPMSG_RC2_40 | IPMSG_RC2_40OLD)
IPMSG_RC2_128ALL = (IPMSG_RC2_128 | IPMSG_RC2_128OLD)
IPMSG_BLOWFISH_128ALL = (IPMSG_BLOWFISH_128 | IPMSG_BLOWFISH_128OLD)

#file types for fileattach command
IPMSG_FILE_REGULAR = 0x00000001
IPMSG_FILE_DIR = 0x00000002
IPMSG_FILE_RETPARENT = 0x00000003   # return parent directory
IPMSG_FILE_SYMLINK = 0x00000004
IPMSG_FILE_CDEV = 0x00000005    # for UNIX
IPMSG_FILE_BDEV = 0x00000006    # for UNIX
IPMSG_FILE_FIFO = 0x00000007    # for UNIX
IPMSG_FILE_RESFORK = 0x00000010    # for Mac

#file attribute options for fileattach command
IPMSG_FILE_RONLYOPT = 0x00000100
IPMSG_FILE_HIDDENOPT = 0x00001000
IPMSG_FILE_EXHIDDENOPT = 0x00002000    # for MacOS X
IPMSG_FILE_ARCHIVEOPT = 0x00004000
IPMSG_FILE_SYSTEMOPT = 0x00008000

#extend attribute types for fileattach command
IPMSG_FILE_UID = 0x00000001
IPMSG_FILE_USERNAME = 0x00000002    # uid by string
IPMSG_FILE_GID = 0x00000003
IPMSG_FILE_GROUPNAME = 0x00000004    # gid by string
IPMSG_FILE_PERM = 0x00000010    # for UNIX
IPMSG_FILE_MAJORNO = 0x00000011    # for UNIX devfile
IPMSG_FILE_MINORNO = 0x00000012    # for UNIX devfile
IPMSG_FILE_CTIME = 0x00000013    # for UNIX
IPMSG_FILE_MTIME = 0x00000014
IPMSG_FILE_ATIME = 0x00000015
IPMSG_FILE_CREATETIME = 0x00000016
IPMSG_FILE_CREATOR = 0x00000020    # for Mac
IPMSG_FILE_FILETYPE = 0x00000021    # for Mac
IPMSG_FILE_FINDERINFO = 0x00000022   # for Mac
IPMSG_FILE_ACL = 0x00000030
IPMSG_FILE_ALIASFNAME = 0x00000040    # alias fname
IPMSG_FILE_UNICODEFNAME = 0x00000041    # UNICODE fname

FILELIST_SEPARATOR = 0x7
HOSTLIST_DUMMY = 0x8
HLIST_ENTRY_SEPARATOR = 0x3a

FEIQ_EXTEND_CMD = 0x600000

def IS_CMD_SET(cmd:int, test:int):
	return ((cmd) & 0xFF) == test

def IS_OPT_SET(cmd:int, opt:int):
	return (cmd & opt) == opt



ENCODETYPE = 'gb2312' #编码方式

PACKET_SEP = b':' #报文内部分割附