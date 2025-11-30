""" ALGORITHM Euclidean GCD
    INPUT: Two positive integers a, b where a ≥ b
    OUTPUT: Greatest Common Divisor (GCD) of a and b

BEGIN
    // Validation: Ensure inputs are positive
    IF a ≤ 0 OR b ≤ 0 THEN
        DISPLAY "Error: Inputs must be positive integers"
        RETURN ERROR
    END IF
    
    // Main algorithm loop
    WHILE b ≠ 0 DO
        // Store current value of b
        temp ← b
        
        // Replace b with remainder of a divided by b
        b ← a MOD b
        
        // Replace a with old value of b
        a ← temp
    END WHILE
    
    // When b becomes 0, a contains the GCD
    RETURN a
END

"""