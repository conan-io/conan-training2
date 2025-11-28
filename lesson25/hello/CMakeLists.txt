cmake_minimum_required(VERSION 3.15)
project(hello CXX)

add_library(hello src/hello.cpp)
target_include_directories(hello PUBLIC include)

set_target_properties(hello PROPERTIES PUBLIC_HEADER "include/hello.h")
install(TARGETS hello)

# Install an empty CMake file just for demonstration purposes
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/cmake/HelloConfig.cmake 
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/share/)
