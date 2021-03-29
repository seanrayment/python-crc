# python-crc

This is a naive python implementation of a cyclic redundancy check (CRC). See the following resources to learn about CRC:

https://zlib.net/crc_v3.txt

https://www.youtube.com/watch?v=izG7qT0EpBw

https://www.cs.jhu.edu/~scheideler/courses/600.344_S02/CRC.html

CRC detects transmission errors by computing a check value to be sent along with a message. The receiver can verify the message against the check value by re-computing it.

The check value is calculated by taking the remainder of our message (in bits) divided by a special value. The special value is carefully chosen to maximize the number of consecutive bits that can change such that the check value will always be different.   

The tricky bit is that we use polynomial representations of the message bitstring and special value in computation, and all operations are in mod 2. 

The intuition behind this is explained best in the resources above, but it turns out that the polynomial approach can detect all burst erorrs in the transmitted message of length less than the degree of the polynomial. 

See this wikipedia entry for a list of polynomial codes used in practice: https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Polynomial_representations_of_cyclic_redundancy_checks

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
