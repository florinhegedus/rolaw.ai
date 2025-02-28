import requests


CODUL_PENAL_LINK = "https://legislatie.just.ro/Public/DetaliiDocument/109855"


def main():
    response = requests.get(CODUL_PENAL_LINK + "#id_artA1468")
    print(response)


if __name__ == '__main__':
    main()