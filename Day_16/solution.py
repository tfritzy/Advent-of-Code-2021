from copy import copy, deepcopy
import math
from os import truncate
from typing import NewType
import queue


def parse_input(input_lines):
    return input_lines[0]


folder = "Day_16"
input_data = parse_input(open(f"{folder}/inputData.txt").readlines())
test_data = "C0015000016115A2E0802F182340"


def get_version(packet):
    return int(packet[:3], 2)


def get_type(packet):
    return int(packet[3:6], 2)


def len_literal(packet):
    index = 6
    bits = packet[index: index + 5]
    while(bits[0] == "1"):
        index += 5
        bits = packet[index: index + 5]
    return index + 5


def literal_value(packet):
    index = 6
    total_value_bits = ""
    bits = packet[index: index + 5]
    total_value_bits += bits[1: 5]
    while(bits[0] == "1"):
        index += 5
        bits = packet[index: index + 5]
        total_value_bits += bits[1: 5]

    return int(total_value_bits, 2)


version_sum = 0


def parse_packet(packet):
    version = get_version(packet)
    print("version: " + str(version))
    global version_sum
    version_sum += version
    type = get_type(packet)
    if (type != 4):
        print("operator")
        # operator
        length_type_id = int(packet[6])
        values = []
        packet_len = 0
        if (length_type_id == 0):
            num_bits_in_sub_packets = int(packet[7:22], 2)
            index = 22
            end_index = index + num_bits_in_sub_packets
            sub_packets = packet[index:end_index]

            while (index < 22 + num_bits_in_sub_packets):
                num_bits, sub_value = parse_packet(sub_packets)
                values.append(sub_value)
                index += num_bits
                sub_packets = packet[index:end_index]

            packet_len = end_index
        elif(length_type_id == 1):
            packet_count = int(packet[7:18], 2)
            packet_index = 0
            bin_index = 18
            while (packet_index < packet_count):
                sub_packets = packet[bin_index:]
                num_bits, sub_value = parse_packet(sub_packets)
                bin_index += num_bits
                values.append(sub_value)
                packet_index += 1

            packet_len = bin_index

        if (type == 0):
            return (packet_len, sum(values))
        elif (type == 1):
            multiplied = values[0]
            for i in range(1, len(values)):
                multiplied *= values[i]
            return (packet_len, multiplied)
        elif(type == 2):
            return (packet_len, min(values))
        elif(type == 3):
            return (packet_len, max(values))
        elif(type == 5):
            return (packet_len, 1 if values[0] > values[1] else 0)
        elif (type == 6):
            return (packet_len, 1 if values[0] < values[1] else 0)
        elif(type == 7):
            return (packet_len, 1 if values[0] == values[1] else 0)

    else:
        # literal
        print("literal")
        return (len_literal(packet), literal_value(packet))


def solve():
    data = input_data
    end_length = len(data) * 4
    packet = bin(int(data, 16))[2:].zfill(end_length)
    print(parse_packet(packet))


solve()
