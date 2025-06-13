cmake_minimum_required(VERSION 3.15)
project(consumer CXX)

find_package(mylib CONFIG REQUIRED)

add_library(consumer src/consumer.cpp)
target_link_libraries(consumer mylib::mylib)
target_include_directories(consumer PUBLIC include)

set_target_properties(consumer PROPERTIES PUBLIC_HEADER "include/consumer.h")
install(TARGETS consumer)
