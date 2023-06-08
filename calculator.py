import numexpr

reshenie = input("Vvedite primer ")

otvet =numexpr.evaluate(reshenie)

print(f'Vot otvet {otvet}')
