#include <iostream>
#include "hello.h"
#include <fmt/color.h>

void hello() {
    #ifdef NDEBUG
    fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold, "hello/1.0: Hello World Release!\n");
    #else
    fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold, "hello/1.0: Hello World Debug!\n");
    #endif
}
