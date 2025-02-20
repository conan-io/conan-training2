#ifdef USE_STD_FORMAT
    #include <format>
    #include <iostream>
#else
    #include <fmt/core.h>
    #include <fmt/color.h>
#endif

int main() {

#ifdef USE_STD_FORMAT
    std::cout << std::format("Conan is a MIT-licensed, Open Source package manager for C and C++ development\n");
#else
    fmt::print(fmt::fg(fmt::color::cyan) | fmt::emphasis::bold, 
               "Conan is a MIT-licensed, Open Source ");
    fmt::print(fmt::fg(fmt::color::white),
               "package manager for C and C++ development\n");
#endif
    return 0;
}
