#ifdef USE_TABULATE
#include <tabulate/table.hpp>
using namespace tabulate;
#else
#include <fmt/core.h>
#include <fmt/color.h>
#endif

int main() {

#ifdef USE_TABULATE
    Table info;
    info.add_row({
        "Conan is MIT-licensed",
        "Open Source package manager",
    #ifdef NDEBUG
        "Release configuration"
    #else
        "Debug configuration"
    #endif
    });
    info[0][0].format().font_color(Color::red).font_style({FontStyle::bold});
    info[0][1].format().font_color(Color::blue).font_style({FontStyle::bold});
    info[0][2].format().font_color(Color::green).font_style({FontStyle::bold});
    std::cout << info << std::endl;
#else
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
#endif

    return 0;
}
