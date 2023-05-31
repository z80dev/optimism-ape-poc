# example vyper contract with a counter
counter: public(uint256)

# external function to increment the counter
@external
def increment():
    self.counter += 1
