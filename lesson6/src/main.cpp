#include <fmt/core.h>
#include <fmt/color.h>

int main() {
    fmt::print(fmt::fg(fmt::color::cyan) | fmt::emphasis::bold, 
               "Conan is a MIT-licensed, Open Source ");
    fmt::print(fmt::fg(fmt::color::white), 
               "package manager for C and C++ development\n");

    #ifdef NDEBUG
    fmt::print(fmt::fg(fmt::color::green) | fmt::emphasis::italic,
               "Release configuration!\n");
    #else
    fmt::print(fmt::fg(fmt::color::yellow) | fmt::emphasis::italic,
               "Debug configuration!\n");
    #endif

    return 0;
}
