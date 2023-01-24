# acetone

a L7-HTTP website attacking method written in Python 3 (PySocks lib)

## Installation

1. Download the script:
```bash
git clone https://github.com/khoi1908vn/acetone.git
```
2. Install the requirements:
```bash
pip install -r requirements.txt
```

## Usage

Import the ``Acetone()`` class and run it in your script:

```python
from acetone import Acetone

url = 'https://example.com'
# 5 for SOCKS5, 4 for SOCKS4 
socks_type = 5
# proxies file path
proxies_path = 'socks5.txt'
# threads to be created to attack
thread_num = 400
# attack time in seconds
attack_time = 120

Acetone(url=url, socks_type=socks_type, proxies_path=proxies_path, thread_num=thread_num, attack_time=attack_time)
```

## Contributing

This project is private and not yet ready to receive pull requests.

After this repo is public, any contribution is appreiciated!

## License

[MIT](https://choosealicense.com/licenses/mit/)
