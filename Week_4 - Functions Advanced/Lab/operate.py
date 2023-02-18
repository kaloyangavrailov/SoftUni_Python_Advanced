def operate(operator, *args):
    integers = args

    def addition(op, nums):
        result = 0
        for el in nums:
            result += el
        return result

    def subtraction(op, nums):
        result = nums[0]
        for el in range(1, len(nums)):
            result -= nums[el]
        return result

    def multiplication(op, nums):
        result = 1
        for el in nums:
            result *= el
        return result

    def division(op, nums):
        result = nums[0]
        if 0 in nums:
            return 0
        for el in range(1, len(nums)):
            result *= nums[el]
        return result

    if operator == '+':
        return addition(operator,integers)

    if operator == '-':
        return subtraction(operator,integers)

    if operator == '*':
        return multiplication(operator,integers)

    if operator == '/':
        return division(operator,integers)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
