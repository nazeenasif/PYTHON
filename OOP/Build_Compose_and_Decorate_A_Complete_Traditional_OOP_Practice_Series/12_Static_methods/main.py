class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
temp_c = TemperatureConverter.celsius_to_fahrenheit(37)

print(temp_c)