from portscanner import Scanner
from grabber import Grabber


def main():
    ip = "localhost"
    portrange = (1, 1001)
    scanner = Scanner(ip)
    scanner.scan(*portrange)

    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print("Error")


if __name__ == "__main__":
    main()
