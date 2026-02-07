list_of_msg = ['mg1', 'ddda', 'wwd', 'gggda']

def print_msg(msg_list:list):
    send = []
    for msg in msg_list:
        print(msg)
        send = send_msg(send, msg)
    print("Send list:", send)
    print("Original list", list_of_msg)

def send_msg(msg_list:list, msg):
    msg_list.append(msg)
    return msg_list

print_msg(list_of_msg)
