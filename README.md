# python-crc

This is a naive implementation of a cyclic redundancy check (CRC). See the following resources to learn about CRC:

https://zlib.net/crc_v3.txt

https://www.youtube.com/watch?v=izG7qT0EpBw

CRC detects transmission errors by computing a check value to be sent along with a message. The receiver can verify the message against the check value by re-computing it.

The check value is calculated by taking the remainder of our message (in bits) divided by a special value. The special value is carefully chosen to optimize the number of consecutive bits that can change such that the check value will always be different.   

The tricky bit is that we use polynomial representations of the message bitstring and special value in computation, and all operations are in mod 2. 

The intuition behind this is explained best in the video above. The idea is that we want the difference between the received message and the transmitted message to look similar when groups of consecutive bits are flipped anywhere in the transmitted message. 

\<handwaving\> In polynomial arithmetic mod 2, there are no carries, so groups of bit flips that happen in different locations in the transmitted message produce received messages that are more predictably different. This ends up making it much easier to choose the special value that we use to compute the check value. \</handwaving\>

### Usage

```python
from crc import CRC

msg = 'Hello, world!'
crc = CRC('1000000100001') # CRC-16-CCITT, used in bluetooth
checksum = crc.checksum(msg)
```

```python
crc.intact('Hello, world!', checksum)
# True
```

```python
crc.intact('Hello, world?', checksum)
# False
```
