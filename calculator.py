def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

def calculator():
    print("Simple Calculator")
    print("Type 'exit' to quit")

    while True:
        user_input = input("Enter an expression: ")

        if user_input.lower() == 'exit':
            break

        result = evaluate_expression(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
