#include <fmt/core.h>
#include <fmt/color.h>

int main() {
    fmt::print(fmt::fg(fmt::color::cyan) | fmt::emphasis::bold, 
               "Conan is a MIT-licensed, Open Source ");
    fmt::print(fmt::fg(fmt::color::white), 
               "package manager for C and C++ development\n");
    return 0;
}
