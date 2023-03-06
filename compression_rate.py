import os

def get_compression_rate(original_path, compressed_path):
    original_file_stats = os.stat(original_path)
    compressed_file_stats = os.stat(compressed_path)

    return 1 - (compressed_file_stats.st_size / original_file_stats.st_size) 

