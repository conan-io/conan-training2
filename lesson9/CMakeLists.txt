cmake_minimum_required(VERSION 3.15)
project(hello CXX)

find_package(fmt)

add_library(hello src/hello.cpp)
target_include_directories(hello PUBLIC include)

set_target_properties(hello PROPERTIES PUBLIC_HEADER "include/hello.h")

target_link_libraries(hello fmt::fmt)

install(TARGETS hello)
