# Define test component directories
TEST_DIRS = $(dir $(wildcard */))
$(info [${TEST_DIRS}])

.PHONY: all $(TEST_DIRS)
all: $(TEST_DIRS)


# Run tests
$(TEST_DIRS):
	make -C $@

# Clearn tests
.PHONY: clean
clean:
	$(foreach DIR, $(TEST_DIRS), make -C $(DIR) clean)