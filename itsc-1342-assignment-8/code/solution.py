# Nabi Honarvaran - Assignment 8

def dissect_packet(src_ip, dst_ip, protocol, payload_bytes, flags=None):
    return {
        "src": src_ip,
        "dst": dst_ip,
        "proto": str(protocol).upper(),
        "length": max(0, int(payload_bytes)),
        "syn_flag": bool(flags is not None and "SYN" in flags),
    }
