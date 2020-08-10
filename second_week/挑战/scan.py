import re, sys, getopt, socket

class Argv():
    """命令行处理"""
    def __init__(self):
        self.args = ''
        self.host = ''
        self.port = ''
        self.opts = self._get_opts()
        self.sort = self._sort_opts()

    def _get_opts(self):
        """获得参数"""
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'h',['host=','port=','help'])
            self.args = args
            return opts
        except getopt.GetoptError:
            print("Parameter Error")
            sys.exit(2)

    def _sort_opts(self):
        """处理参数"""
        for opt, arg in self.opts:
            if opt in ('-h','--help'):
                print("scan.py --host IP --port PORT1-PORT2")
                sys.exit(1)
            if opt == '--host':
                p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
                if p.match(arg):
                    self.host = arg
                else:
                    print("Parameter Error")
                    sys.exit(1)
            if opt == '--port':
                if '-' in arg:
                    port = arg.split('-')
                else:
                    port = [arg, arg]
                self.port = [port[0],port[1]]

args =Argv()

class Scan(object):
    """端口扫描类"""
    def __init__(self):
        self.open_port = ''
        self.closed_port = ''
        self.get_scan = self._get_scan()

    def _get_scan(self):
        """扫描端口"""
        self.open_port = []
        self.closed_port = []
        for port in range(int(args.port[0]), int(args.port[1])+1):
            s = socket.socket()
            s.settimeout(0.1)
            if s.connect_ex((args.host, port)) == 0:
                self.open_port.append(port)
            else:
                self.closed_port.append(port)
        for port in args.args:
            if s.connect_ex((args.host, int(port))) == 0:
                self.open_port.append(port)
            else:
                self.closed_port.append(port)

    def export(self):
        for port in self.open_port:
            print("{} open".format(port))
        for port in self.closed_port:
            print("{} closed".format(port))


if __name__ == "__main__":
    scan = Scan()
    scan.export()
