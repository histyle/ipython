import configparser
import paramiko
'''
读取配置文件信息
'''
conf = configparser.ConfigParser()
conf.read("hosts.ini")

host=conf.get('deployment','host')
user=conf.get('deployment','user')
port=conf.get('deployment','port')

print(host,user,port)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host,port,user,"123456")

