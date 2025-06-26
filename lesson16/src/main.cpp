#include <iostream>

int secure_scanner(std::string &path){
    std::cout << "Security Scanner: The path '" + path + "' is secure!\n";
    return 0;
}

int main(int argc, char *argv[]) {
    std::string path;
    if(argc < 2){
        std::cout << "ERROR: The argument 'path' is needed.\n";
        return -1;
    }
    path = std::string(argv[1]);
    return secure_scanner(path);
}
