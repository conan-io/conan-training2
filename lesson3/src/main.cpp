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
        "Conan is an Open Source package manager"
    });
    info[0][0].format().font_color(Color::green).font_style({FontStyle::bold});
    std::cout << info << std::endl;
#else
    fmt::print(fmt::fg(fmt::color::cyan) | fmt::emphasis::bold, 
               "Conan is an Open Source package manager\n");
#endif

    return 0;
}
