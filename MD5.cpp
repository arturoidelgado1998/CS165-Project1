#include <iostream>
#include <string>

const std::string base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

std::string md5_Crypt();
std::string to64(char, int);

int main(int argC, char**argV)
{

}

std::string md5_Crypt()
{
	std::string h;
	return to64((h[0] << 16) | (h[6] << 8) | (h[12]), 4) + 
		   to64((h[1] << 16) | (h[7] << 8) | (h[13]), 4) + 
		   to64((h[2] << 16) | (h[8] << 8) | (h[14]), 4) +
		   to64((h[3] << 16) | (h[9] << 8) | (h[15]), 4) + 
		   to64((h[4] << 16) | (h[10] << 8) | (h[5]), 4) + 
		   to64(h[11], 2);
}

std::string to64(char v, int n)
{
	std::string ret = "";
	for(unsigned int i = 0; i<n;i++)
	return std::string();
}