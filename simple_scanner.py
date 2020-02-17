from socket import *

def Port_Range(m_range):

    sep_param_list = [' ', ',']

    for sep_param in sep_param_list:
        if sep_param in m_range:
            return [int(port) for port in m_range.split(sep_param)]

    if '-' in m_range:
        port_start, port_end = m_range.split('-')
        return range(int(port_start), int(port_end))

    try:
        return [int(m_range)]

    except:
        exit('정상적인 포트를 지정하시오')


if __name__=="__main__":

    open_port_list = [];    open_port_list: list

    victim_ip = input('insert victim ip : ')

    for port in Port_Range(input("Port Scan Range (ex:80, 1-1024) : ")):

        try:
            sc = socket(AF_INET,SOCK_STREAM)
            sc.settimeout(0.5)
            print("trying... [ %s ]" % port)
            sc.connect((victim_ip,port))
            open_port_list.append(port)

        except Exception as msg:
            print(msg,"\n")

    if len(open_port_list) > 0:
        [print("[ %s ] is open" % open) for open in open_port_list]
    else:
        print("Nothing Found... [%s]" % victim_ip)