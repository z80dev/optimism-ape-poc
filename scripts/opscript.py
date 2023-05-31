from ape import project, accounts

def main():
    # import account
    account = accounts.load('tester')

    # create contract
    contract = project.Example.deploy(sender=account)

    # run functions
    receipt_1 = contract.increment(sender=account)
    receipt_2 = contract.increment(sender=account)
