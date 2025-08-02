def safe_divide(numerator, denominator):
    try:
        #convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        #peform division
        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."