from validator_collection import validators, checkers, errors

email_address = validators.email('test@domain.dev')
print(email_address)
