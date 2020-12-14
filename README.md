# newnewthaicut

It's a newnewthaicut powered by newmm and ThaiNER from PyThaiNLP.

```python
from pythainlp import word_tokenize as pythainlpcut
pythainlpcut("ผมชื่อนายวรรณพงษ์ ภัททิยไพบูลย์ ผมเป็นคนไทยเรียนที่มหาวิทยาลัยขอนแก่น")
# output: ['ผม', 'ชื่อ', 'นาย', 'วรรณ', 'พงษ์', ' ', 'ภัททิย', 'ไพบูลย์', ' ', 'ผม', 'เป็น', 'คนไทย', 'เรียน', 'ที่', 'มหาวิทยาลัยขอนแก่น']
from newnewthaicut import word_tokenize
word_tokenize("ผมชื่อนายวรรณพงษ์ ภัททิยไพบูลย์ ผมเป็นคนไทยเรียนที่มหาวิทยาลัยขอนแก่น")
# output: ['ผม', 'ชื่อ', 'นายวรรณพงษ์ ภัททิยไพบูลย์', ' ', 'ผม', 'เป็น', 'คนไทย', 'เรียน', 'ที่', 'มหาวิทยาลัยขอนแก่น']
```

Author: Wannaphong Phatthiyaphaibun