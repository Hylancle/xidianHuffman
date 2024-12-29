from huffman import HuffmanCoding
import os
path = "example.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

file_size = os.path.getsize("example.bin")
print(f"文件 example.bin 的大小为 {file_size} 字节。")
decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)

file_size = os.path.getsize(decom_path)
print(f"文件 {decom_path} 的大小为 {file_size} 字节。")