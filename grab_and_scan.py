from portscanner import Scanner
from grabber import Grabber


def main():
    ip = "localhost"
    portrange = (1, 1001)
    scanner = Scanner(ip)
    scanner.scan(*portrange)

    for port in scanner.open_ports:
        grabber = Grabber(ip, port)
        print(grabber.read())
        grabber.close()


if __name__ == "__main__":
    main()
