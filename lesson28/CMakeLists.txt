cmake_minimum_required(VERSION 3.15)
project(hello CXX)

add_library(hello src/hello.cpp)
target_include_directories(hello PUBLIC include)

set_target_properties(hello PROPERTIES PUBLIC_HEADER "include/hello.h")

find_package(fmt)
target_link_libraries(hello fmt::fmt)
target_compile_definitions(hello PRIVATE USING_FMT=1)

install(TARGETS hello)
