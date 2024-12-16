#!/bin/python3

import sys
import binascii

DISK_IMAGE = sys.argv[1]
MBR_SIZE = 512
GPT_HEADER_OFFSET = 512
GPT_HEADER_SIZE = 92
APFS_GPT_PARTITION_UUID = "7C3457EF-0000-11AA-AA11-00306543ECAC"
PARTITION_ENTRY_SIZE = 128
DEFAULT_SECTOR_SIZE = 4096
SUPERBLOCK_MAGIC = b'\x4e\x58\x53\x42'

def hex_to_int(hex_str):
    """Convert a hex string to an integer."""
    hex_str = binascii.hexlify(hex_str)
    print(hex_str)
    return int(hex_str, 16)


def convert_to_gb(number_of_blocks, block_size):
    """Convert the number of blocks to GiB."""
    block_size = hex_to_int(number_of_blocks) * hex_to_int(block_size) / (1024**3)
    return round(block_size, 0)


def find_superblock(f):
    f.seek(0, 2)
    file_size = f.tell()
    f.seek(0)
    
    while f.tell() < file_size:
        data = f.read(DEFAULT_SECTOR_SIZE)
        if SUPERBLOCK_MAGIC in data:
            offset = f.tell() - DEFAULT_SECTOR_SIZE + data.index(SUPERBLOCK_MAGIC)
            print(f"Superblock magic number found at offset: {offset}")
            return offset
    print("Superblock magic number not found.")
    return None

nx_block_size = 0x24
nx_block_count = 0x28


    


def read_object_header(data):
    """Function to read the object header of an APFS object, according to Rune Nordvik's APFS specification Page 6."""
    
    data = data[::-1]

    if len(data) < 32:
        return None

    fletcher_checksum = binascii.hexlify(data[24:])
    object_id = binascii.hexlify(data[16:24])
    transaction_id = binascii.hexlify(data[8:16])
    obj_type = binascii.hexlify(data[4:8])
    obj_subtype = binascii.hexlify(data[0:4])


    #print(f"Fletcher Checksum:\t{fletcher_checksum}\nObject ID:\t\t{object_id}\nTransaction ID:\t\t{transaction_id}\nObject Type:\t\t{obj_type}\nObject Subtype:\t\t{obj_subtype}")
    
    return {
        'fletcher_checksum': fletcher_checksum,
        'object_id': object_id,
        'transaction_id': transaction_id,
        'object_type': obj_type,
        'object_subtype': obj_subtype
    }


object_type = {
    '0x00000001': 'OBJECT_TYPE_NX_SUPERBLOCK',
    '0x00000002': 'OBJECT_TYPE_BTREE',
    '0x0000000b': 'OBJECT_TYPE_OMAP',
    '0x0000000d': 'OBJECT_TYPE_FS',
    '0x0000000e': 'OBJECT_TYPE_FS_TREE',
    '0x00000000': 'OBJECT_TYPE_INVALID',
    '0x0000ffff': 'OBJECT_TYPE_MASK',
    '0xffff0000': 'OBJECT_TYPE_FLAGS_MASK',
}

obj_type_flags = {
    '0x00000000': 'OBJ_VIRTUAL',
    '0x80000000': 'OBJ_EPHEMERAL',
    '0x40000000': 'OBJ_PHYSICAL',
    '0x20000000': 'OBJ_NOHEADER',
    '0x10000000': 'OBJ_ENCRYPTED',
    '0x08000000': 'OBJ_NONPERSISTENT'
}

if __name__ == "__main__":
    print("APFS Parser\n")

    test_object_header = b'\x15\xfd\x6f\xf8\x2d\xa1\xde\x43\x01\x00\x00\x00\x00\x00\x00\x00\x0e\x81\x58\x00\x00\x00\x00\x00\x01\x00\x00\x80\x00\x00\x00\x00'
    object_header = read_object_header(test_object_header)

    print("Object Header")
    print(f"{80*'-'}")
    print(object_header)
    print(f"{80*'-'}")

    with open(DISK_IMAGE, "rb") as f:
        gpt_header = f.read(GPT_HEADER_SIZE)
        print("GPT Header: ", binascii.hexlify(gpt_header))
        sb_offset = find_superblock(f)
        f.seek(sb_offset + 4)
        block_size = f.read(4)
        f.seek(sb_offset + 8)
        number_of_blocks = f.read(8)
        print("Block Size: ", binascii.hexlify(block_size))
        print("Number of Blocks: ", binascii.hexlify(number_of_blocks))
        print("Size of the block: ", convert_to_gb(number_of_blocks, block_size), "GiB")

   

