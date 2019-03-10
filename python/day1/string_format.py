# Print string
print('%s %s' % ('one','two'))
# Print string with tab indentation
print('%s \t\t %s' % ('one','two'))

# Printing Decimal 
print('%d %d' %(1,2))
# Print Decimal and String
print('%d %s' %(1,"2"))
# Print Decimal and Float
print('%d %f' %(1,2.0))

# New Format for printing 
print('{} {}'.format(1, 2))
print('{1} {0}'.format(1, 2))

# Old format for right aligning string
print('%15s' % ("hello"))
# New format for right aligning string 
print('{:>15}'.format("hello"))

# Left align string
print('{:15} {:15}'.format("NAME","DESCRIPTION"))


# Padding character 
print('{:_<15}'.format("NAME"))

# Center Align
print('{:^10}'.format('test'))

# Printing Float with fix decimal length
print('{:06.2f}'.format(3.141592653589793))
