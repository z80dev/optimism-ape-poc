from ape import project, accounts
import ape

def main():
    # import account
    account = accounts.load('tester')
    account.set_autosign(True, " ")

    # create contract
    # contract = project.Example.deploy(sender=account)
    contract = project.Example.deployments[-1]
    # contract = project.Example.at("0xf93e243e8C3746646DBb8ca3f90087cb6178a617")

    # run functions
    with ape.reverts():
        receipt_1 = contract.increment(sender=account)
    # receipt_2 = contract.increment(sender=account)
