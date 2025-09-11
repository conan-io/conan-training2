#include "../include/hello.h"
#include "gtest/gtest.h"

namespace {
    TEST(HelloTest, ComposeMessagesEmpty) {
        EXPECT_EQ(std::string("hello/1.0: Hello World ! ()\n"), 
                  compose_message("", ""));
    }

    TEST(HelloTest, ComposeMessagesSpecialChars) {
        EXPECT_EQ(std::string("hello/1.0: Hello World Special! (with spaces & symbols!)\n"), 
                  compose_message("Special", "with spaces & symbols!"));
    }
}
