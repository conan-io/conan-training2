cmake_minimum_required(VERSION 3.15)
project(formatter CXX)

add_executable(formatter src/main.cpp)

if (USE_TABULATE)
    find_package(tabulate REQUIRED)
    target_link_libraries(formatter tabulate::tabulate)
    target_compile_definitions(formatter PRIVATE USE_TABULATE)
else()
    find_package(fmt REQUIRED)
    target_link_libraries(formatter fmt::fmt)
endif()
