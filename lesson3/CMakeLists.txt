cmake_minimum_required(VERSION 3.15)
project(formatter CXX)

add_executable(formatter src/main.cpp)

if (USE_STD_FORMAT)
    target_compile_definitions(formatter PRIVATE USE_STD_FORMAT)
else()
    find_package(fmt REQUIRED)
    target_link_libraries(formatter fmt::fmt)
endif()
