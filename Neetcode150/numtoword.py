def numtoword(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    Tens = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Nintey"]
    result =""
    if num < 0:
        return "Number cannot be Negative"
    if num == 0:
        return "Zero"
    if num < 20:
        return ones[num]
    if num < 100:
        return Tens[num // 10] + " " + ones[num % 10]
    if num < 1000:
        return numtoword(num // 100) + " " + "Hundred" + " " + numtoword(num % 100)
    if num < 1000000:
        return numtoword(num // 1000) + " " + "Thousand" + " " + numtoword(num% 1000)
    if num < 1000000000:
        return numtoword(num // 1000000) + " " + "Million" + " " + numtoword(num % 1000000)
    if num < 1000000000000:
        return numtoword(num // 1000000000) + " " + "Billion" + " " + numtoword(num % 1000000000)
    else:
        return "Out of Range"

number = int(input("Enter the Number:"))
print(numtoword(number))