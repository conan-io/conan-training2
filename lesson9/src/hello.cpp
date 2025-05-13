#include <iostream>
#include "hello.h"

#if USING_FMT == 1
#include <fmt/color.h>
#endif

void hello() {
    #if USING_FMT == 1
        fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold, 
                   "hello/1.0: Hello World! (with color!)\n");
    #else
        std::cout << "hello/1.0: Hello World! (without color)" 
                  << std::endl;
    #endif
}
