#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <net/if.h>        //for struct ifreq
typedef unsigned char uint8_t;
int get_mac(uint8_t * mac, int len_limit) {  //返回值是实际写入char * mac的字符个数（不包括'\0'）
	struct ifreq ifreq;
	int sock;

	if ((sock = socket (AF_INET, SOCK_STREAM, 0)) < 0) {
		perror ("socket");
		return -1;
	}
	strcpy (ifreq.ifr_name, "eth0");    //Currently, only get eth0

	if (ioctl (sock, SIOCGIFHWADDR, &ifreq) < 0) {
		perror ("ioctl");
		return -1;
	}
	//git mac,output.
	return snprintf (mac, len_limit, "%06X%02X%02X%02X%02X%02X",
	                 (uint8_t) ifreq.ifr_hwaddr.sa_data[0], \
	                 (uint8_t) ifreq.ifr_hwaddr.sa_data[1], \
	                 (uint8_t) ifreq.ifr_hwaddr.sa_data[2], \
	                 (uint8_t) ifreq.ifr_hwaddr.sa_data[3], \
	                 (uint8_t) ifreq.ifr_hwaddr.sa_data[4], \
	                 (uint8_t) ifreq.ifr_hwaddr.sa_data[5]);
}
int main(int argc, const char** argv){
	uint8_t Mac[17] = {0};
	int nRtn = get_mac(Mac, sizeof(Mac));  //获取Mac地址
	printf("%s\n", Mac);
}
