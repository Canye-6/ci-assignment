from api import get_status


def main():
    status = get_status()
    print(f"System status: {status}")


if __name__ == "__main__":
    main()


