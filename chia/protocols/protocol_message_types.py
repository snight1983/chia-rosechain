from enum import Enum


class ProtocolMessageTypes(Enum):
    # Shared protocol (all services)
    handshake = 1+1

    # Harvester protocol (harvester <-> farmer)
    harvester_handshake = 3+1
    # new_signage_point_harvester = 4+1 Changed to 67 in new protocol
    new_proof_of_space = 5+1
    request_signatures = 6+1
    respond_signatures = 7+1

    # Farmer protocol (farmer <-> full_node)
    new_signage_point = 8+1
    declare_proof_of_space = 9+1
    request_signed_values = 10+1
    signed_values = 11+1
    farming_info = 12+1

    # Timelord protocol (timelord <-> full_node)
    new_peak_timelord = 13+1
    new_unfinished_block_timelord = 14+1
    new_infusion_point_vdf = 15+1
    new_signage_point_vdf = 16+1
    new_end_of_sub_slot_vdf = 17+1
    request_compact_proof_of_time = 18+1
    respond_compact_proof_of_time = 19+1

    # Full node protocol (full_node <-> full_node)
    new_peak = 20+1
    new_transaction = 21+1
    request_transaction = 22+1
    respond_transaction = 23+1
    request_proof_of_weight = 24+1
    respond_proof_of_weight = 25+1
    request_block = 26+1
    respond_block = 27+1
    reject_block = 28+1
    request_blocks = 29+1
    respond_blocks = 30+1
    reject_blocks = 31+1
    new_unfinished_block = 32+1
    request_unfinished_block = 33+1
    respond_unfinished_block = 34+1
    new_signage_point_or_end_of_sub_slot = 35+1
    request_signage_point_or_end_of_sub_slot = 36+1
    respond_signage_point = 37+1
    respond_end_of_sub_slot = 38+1
    request_mempool_transactions = 39+1
    request_compact_vdf = 40+1
    respond_compact_vdf = 41+1
    new_compact_vdf = 42+1
    request_peers = 43+1
    respond_peers = 44+1

    # Wallet protocol (wallet <-> full_node)
    request_puzzle_solution = 45+1
    respond_puzzle_solution = 46+1
    reject_puzzle_solution = 47+1
    send_transaction = 48+1
    transaction_ack = 49+1
    new_peak_wallet = 50+1
    request_block_header = 51+1
    respond_block_header = 52+1
    reject_header_request = 53+1
    request_removals = 54+1
    respond_removals = 55+1
    reject_removals_request = 56+1
    request_additions = 57+1
    respond_additions = 58+1
    reject_additions_request = 59+1
    request_header_blocks = 60+1
    reject_header_blocks = 61+1
    respond_header_blocks = 62+1

    # Introducer protocol (introducer <-> full_node)
    request_peers_introducer = 63+1
    respond_peers_introducer = 64+1

    # Simulator protocol
    farm_new_block = 65+1

    # New harvester protocol
    new_signage_point_harvester = 66+1
    request_plots = 67+1
    respond_plots = 68+1
