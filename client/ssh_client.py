import paramiko


class SshClient:
    """ssh连接"""

    def __init__(self, host, password, username="root", port=22):
        self.host = host
        self.username = username
        self.port = port
        self.password = password
        # self.pkey = paramiko.RSAKey.from_private_key(StringIO(PRIVATE_KEY))

    def get_ssh(self):
        """主机连接"""
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )  # 允许链接不在know_hosts文件中的主机
        ssh.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            # pkey=self.pkey,
        )
        return ssh

    def execute_cmd(self, cmd):
        """
        执行命令
        cmd: 命令行
        return: 终端输出
        """
        ssh = self.get_ssh()
        stdin, stdout, stderr = ssh.exec_command(cmd)
        ssh.close()
        return stdin, stdout.read().decode(), stderr.read().decode()

    def file_transfer(self, from_path, to_path):
        """
        传输文件
        from_path: 要上传的文件路径(包括文件名),例: scripts-frame/a.sh
        to_path: 上传后文件路径(包括文件名),例: /root/a.sh
        """
        sftp = paramiko.Transport(sock=(self.host, self.port))
        sftp.connect(username=self.username, password=self.password)
        files = paramiko.SFTPClient.from_transport(sftp)
        files.put(from_path, to_path)
        sftp.close()
