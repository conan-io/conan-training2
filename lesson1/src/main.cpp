#include <fmt/core.h>
#include <fmt/color.h>

int main() {
    fmt::print(fmt::fg(fmt::color::cyan) | fmt::emphasis::bold, "Conan is a ");
    fmt::print(fmt::fg(fmt::color::yellow) | fmt::emphasis::bold, "MIT-licensed, ");
    fmt::print(fmt::fg(fmt::color::green) | fmt::emphasis::bold, "Open Source ");
    fmt::print(fmt::fg(fmt::color::white), "package manager for ");
    fmt::print(fmt::fg(fmt::color::magenta) | fmt::emphasis::bold, "C and C++ development\n");
    return 0;
}
