import sys
import struct
import io

try:
    f = io.BytesIO(sys.stdin.buffer.read())
    header = f.read(44)

    if len(header) < 44:
        raise Exception()

    riff, file_size, wave, fmt, length, forma, channels, sample_rate, calculate, block_align, bits_per_sample, data_marker, data_size = struct.unpack("<4sI4s4sIHHIIHH4sI", header[:44])
    if riff != b"RIFF":
        raise Exception()
    if wave != b"WAVE":
        raise Exception()
    if fmt != b"fmt ":
        raise Exception()
    if data_marker != b"data":
        raise Exception()
    print(f"Size={file_size}, Type={forma}, Channels={channels}, Rate={sample_rate}, Bits={bits_per_sample}, Data size={data_size}")

except Exception as e:
    print("NO")
