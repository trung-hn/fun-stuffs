# %%
import requests


def main():
    res = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")

    words = res.text.split()
    words = [w for w in words if len(w) == 5]
    print(*words, sep="\n")


if __name__ == "__main__":
    main()

# %%
